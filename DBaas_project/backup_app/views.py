from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django_cron import CronJobBase, Schedule
# from django_cron import CronJobManager
# from crontab import CronTab
import subprocess
import json
import os
from django.views.decorators.csrf import csrf_exempt
from crontab import CronTab
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import tempfile
from userAuth_app.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from userAuth_app.permissions import IsAllowedRole
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

CONFIG_DIR = '/etc/barman.d'
PGPASS_FILE = os.path.join(os.path.expanduser("~barman"), ".pgpass")
AUTH_KEYS_FILE = os.path.join(os.path.expanduser("~barman"), ".ssh/authorized_keys")

S3_CREDENTIALS_DIR = "/var/lib/barman/.s3-creds"


def execute_command(command, storage_method, username):
   
    try:
        if storage_method not in ['nfs', 's3']:
            return {'status': 'error', 'message': 'Invalid storage method specified.'}

        # Choose the appropriate Barman configuration file
        # config_file = f'/etc/barman-{storage_method}.conf'
        if username == "":
            return {'status': 'error', 'message': 'Invalid value in Username.'}
        config_file = f'/etc/barman.d/{username}/barman-{storage_method}.conf'

        # Insert --format json after the barman command
        command_with_json_format = command[:1] + ['-c', config_file, '--format', 'json'] + command[1:]

        # Execute the modified command
        result = subprocess.run(command_with_json_format, capture_output=True, text=True, check=True)
        return {'status': 'success', 'message': json.loads(result.stdout)}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

def remove_mount_point_from_fstab(mount_point):
    try:
        # Create a temporary file to store the modified fstab content
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            with open('/etc/fstab', 'r') as fstab_file:
                for line in fstab_file:
                    if mount_point not in line:
                        tmp_file.write(line)

        # Replace the original fstab file with the modified one using subprocess
        subprocess.run(['sudo', 'mv', tmp_file.name, '/etc/fstab'], check=True)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def check_server_status(request):
    server_name = request.data.get('server_name')
    storage_method = request.data.get('storage_method')
    username = request.user

    if not server_name:
        return Response({'status': 'error', 'message': 'Server name is required.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(execute_command(['barman', 'check', server_name], storage_method, username))


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_servers(request):
    storage_method = request.query_params.get('storage_method')
    username = request.user

    if not storage_method:
        return Response({'status': 'error', 'message': 'Storage method is required.'}, status=status.HTTP_400_BAD_REQUEST)

    result = execute_command(['barman', 'list-servers'], storage_method, username)
    return Response(result)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_backups(request):
    server_name = request.query_params.get('server_name')
    storage_method = request.query_params.get('storage_method')
    username = request.user

    if not server_name:
        return Response({'status': 'error', 'message': 'Server name is required.'}, status=status.HTTP_400_BAD_REQUEST)

    result = execute_command(['barman', 'list-backups', server_name], storage_method, username)
    return Response(result)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_backup(request):
    server_name = request.query_params.get('server_name')
    backup_name = request.query_params.get('backup_name')
    storage_method = request.query_params.get('storage_method')
    username = request.user
    retention_str = request.query_params.get('retention')

    if not server_name:
        return Response({'status': 'error', 'message': 'Server name is required.'}, status=status.HTTP_400_BAD_REQUEST)

    if retention_str:
        # Proceed with scheduling the backup if no existing cron job found
        config_file_path = os.path.join(CONFIG_DIR, f'{username}/server_config/{storage_method}/{server_name}.conf')
        with open(config_file_path, 'a') as config_file:
            for retention in retention_str.split('\n'):
                if retention and retention != '-1':  # Skip if retention is -1
                    value, unit = int(retention[:-1]), retention[-1]
                    if unit == 'd':
                        server_config = f"retention_policy = RECOVERY WINDOW OF {value} DAYS\n"
                    elif unit == 'm':
                        server_config = f"retention_policy = RECOVERY WINDOW OF {value} MONTHS\n"
                    elif unit == 'y':
                        server_config = f"retention_policy = RECOVERY WINDOW OF {value} YEARS\n"
                    config_file.write(server_config)

    command = ['barman', 'backup', server_name]
    if backup_name:
        command.extend(['--name', backup_name])

    return Response(execute_command(command, storage_method, username))

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def switch_wal(request):
    server_name = request.data.get('server_name')
    storage_method = request.data.get('storage_method')
    username = request.user

    if not server_name:
        return Response({'status': 'error', 'message': 'Server name is required.'}, status=status.HTTP_400_BAD_REQUEST)

    command = ['barman', 'switch-wal', '--force', '--archive', server_name]

    return Response(execute_command(command, storage_method, username))

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def recover_backup(request):
    server_name = request.query_params.get('server_name')
    backup_id = request.query_params.get('backup_id')
    destination_directory = request.query_params.get('destination_directory')
    target_server_name = request.query_params.get('target_server_name')
    storage_method = request.query_params.get('storage_method')
    username = request.user

    if not (server_name, backup_id, destination_directory, target_server_name):
        return Response({'status': 'error', 'message': 'All parameters are required.'}, status=status.HTTP_400_BAD_REQUEST)

    command = ['barman', 'recover', '--remote-ssh-command', f'ssh postgres@{target_server_name}',
               server_name, backup_id, destination_directory]

    return Response(execute_command(command, storage_method, username))

@csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def schedule_backup(request):
    server_name = request.query_params.get('server_name')
    storage_method = request.query_params.get('storage_method')
    retention_str = request.query_params.get('retention')  
    username = request.user.username
    #username = request.user
    schedule_hour = request.query_params.get('schedule_hour','0')
    schedule_minute = request.query_params.get('schedule_minute','0')
    schedule_day = request.query_params.get('schedule_day')  

    if not (server_name, storage_method, retention_str):
        return JsonResponse({'status': 'error', 'message': 'All parameters are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        cron = CronTab(user=True)

        # Check if a cron job already exists for the specified server
        for job in cron:
            command = job.command
            if command.startswith('barman') and server_name in command:
                return Response({'status': 'error', 'message': f'A cron job already exists for server "{server_name}".'}, status=500)

        # Proceed with scheduling the backup if no existing cron job found
        config_file_path = os.path.join(CONFIG_DIR, f'{username}/server_config/{storage_method}/{server_name}.conf')
        with open(config_file_path, 'a') as config_file:
            for retention in retention_str.split('\n'):
                if retention and retention != '-1':  # Skip if retention is -1
                    value, unit = int(retention[:-1]), retention[-1]
                    if unit == 'd':
                        server_config = f"retention_policy = RECOVERY WINDOW OF {value} DAYS\n"
                    elif unit == 'm':
                        server_config = f"retention_policy = RECOVERY WINDOW OF {value} MONTHS\n"
                    elif unit == 'y':
                        server_config = f"retention_policy = RECOVERY WINDOW OF {value} YEARS\n"
                    config_file.write(server_config)

        config_file = f'/etc/{username}/barman-{storage_method}.conf'
        command = f'barman -c {config_file} backup {server_name}'

        job = cron.new(command=command)
        if schedule_hour:
            job.hour.on(schedule_hour)
        if schedule_minute:
            job.minute.on(schedule_minute)

        # Set the day of the week or month based on the schedule_day parameter
        DAY_MAPPING = {
                    'Sunday': 0,
                    'Monday': 1,
                    'Tuesday': 2,
                    'Wednesday': 3,
                    'Thursday': 4,
                    'Friday': 5,
                    'Saturday': 6
                }

        if schedule_day:
            if schedule_day.isdigit() and schedule_day != '':
                # Day of the month (1-31)
                job.day.on(int(schedule_day))
            elif schedule_day in DAY_MAPPING:
                # Day of the week (0-6)
                numeric_day = DAY_MAPPING[schedule_day]
                #numeric_day = DAY_MAPPING[schedule_day.upper()]
                job.dow.on(numeric_day)

        cron.write()


        return Response({'status': 'success', 'message': f'Backup scheduled for {server_name}'}, status=200)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_scheduled_servers(request):
    username = request.user.username
    #username = request.user 
    storage_method = request.query_params.get('storage_method')
    try:
        cron = CronTab(user=True)
        scheduled_servers = []

        # Iterate over all cron jobs to find scheduled servers
        for job in cron:
            command = job.command
            if command.startswith('barman') and 'backup' in command:
                parts = command.split()
                server_name_index = parts.index('backup') + 1
                if server_name_index < len(parts):
                    server_name = parts[server_name_index]
                    config_file_path = os.path.join(CONFIG_DIR, f'{username}/server_config/{storage_method}/{server_name}.conf')
                    if os.path.exists(config_file_path):
                        scheduled_servers.append({
                            'server_name': server_name,
                            'scheduled_time': f"{job.minute} {job.hour} {job.day} {job.month} {job.dow}"
                        })

        # Now, iterate over scheduled servers to find retention period
        servers_with_retention = []
        for server in scheduled_servers:
            retention_period = None
            config_file_path = os.path.join(CONFIG_DIR, f'{username}/server_config/{storage_method}/{server["server_name"]}.conf')
            if os.path.exists(config_file_path):
                with open(config_file_path, 'r') as config_file:
                    for line in config_file:
                        if line.startswith('retention_policy'):
                            retention_period = line.split('=')[-1].strip()[18:]  # Extract retention days
                            break
            servers_with_retention.append({'server_name': server['server_name'], 'retention_period': retention_period, 'scheduled_time': server['scheduled_time']})


        return Response({'status': 'success', 'message': servers_with_retention}, status=200)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_scheduled_backup(request):  
    try:
        server_name = request.query_params.get('server_name')
        storage_method = request.query_params.get('storage_method')
        retention_str = request.query_params.get('retention')
        remove_job = request.query_params.get('remove_job')
        username = request.user.username
        #username = request.user 
        schedule_hour = request.query_params.get('schedule_hour', '0')
        schedule_minute = request.query_params.get('schedule_minute', '0')
        schedule_day = request.query_params.get('schedule_day')


        if not (server_name, storage_method):
            return Response({'status': 'error', 'message': 'Server name and storage method are required.'}, status=500)
            


        config_file_path = os.path.join(CONFIG_DIR, f'{username}/server_config/{storage_method}/{server_name}.conf')
        retention_policy_line = "retention_policy"

        cron = CronTab(user=True)


        if remove_job == 'true':
            # Remove existing cron jobs for the specified server
            for job in cron:
                command = job.command
                if command.startswith('barman') and server_name in command:
                    cron.remove(job)

            with open(config_file_path, 'r') as config_file:
                lines = config_file.readlines()

            with open(config_file_path, 'w') as config_file:
                for line in lines:
                    # Check if the line is not a retention policy line
                    if not line.startswith(retention_policy_line):
                        config_file.write(line)
        
            cron.write()
            return Response({'status': 'success', 'message': 'Scheduled backup removed successfully.'}, status=200)

    # Reschedule the backup job
        for job in cron:
            command = job.command
            if command.startswith('barman') and server_name in command and username in command:
                cron.remove(job)  # Delete the existing cron job that matches the criteria

        new_job = cron.new(command=f"barman -c /etc/barman.d/{username}/barman-{storage_method}.conf backup {server_name}")

        # Check if schedule_minute and schedule_hour are provided and not empty
        if schedule_minute:
            new_job.minute.on(schedule_minute)
        if schedule_hour:
            new_job.hour.on(schedule_hour)
        DAY_MAPPING = {
                'Sunday': 0,
                'Monday': 1,
                'Tuesday': 2,
                'Wednesday': 3,
                'Thursday': 4,
                'Friday': 5,
                'Saturday': 6
            }
        if schedule_day:
            if schedule_day.isdigit() and schedule_day != '':
                # Day of the month (1-31)
                new_job.day.on(int(schedule_day))
            elif schedule_day in DAY_MAPPING:
                # Day of the week (0-6)
                numeric_day = DAY_MAPPING[schedule_day]
                new_job.dow.on(numeric_day)

        cron.write()
        
        if retention_str:
            if retention_str == '-1':
                with open(config_file_path, 'r') as config_file:
                    lines = config_file.readlines()

                with open(config_file_path, 'w') as config_file:
                    for line in lines:
                        # Check if the line is not a retention policy line
                        if not line.startswith(retention_policy_line):
                            config_file.write(line)
                return Response({'status': 'success', 'message': 'Retention period disabled successfully.'}, status=200)

            else:
                with open(config_file_path, 'r') as config_file:
                    lines = config_file.readlines()

                # Open the file in write mode to update retention policy
                with open(config_file_path, 'w') as config_file:
                    # Flag to check if retention policy is updated
                    retention_updated = False
                    for line in lines:
                        if line.startswith('retention_policy'):
                            # Update the existing retention policy with new values
                            retention_policy = []
                            for retention in retention_str.split('\n'):
                                if retention:
                                    value, unit = int(retention[:-1]), retention[-1]
                                    if unit == 'd':
                                        retention_policy.append(f"RECOVERY WINDOW OF {value} DAYS")
                                    elif unit == 'm':
                                        retention_policy.append(f"RECOVERY WINDOW OF {value} MONTHS")
                                    elif unit == 'y':
                                        retention_policy.append(f"RECOVERY WINDOW OF {value} YEARS")
                            # Write the updated retention policy to the file
                            config_file.write(f"retention_policy = {' AND '.join(retention_policy)}\n")
                            retention_updated = True
                        else:
                            # Write other lines back to the file
                            config_file.write(line)

                    # If retention policy is not updated, add a new one
                    if not retention_updated:
                        retention_policy = []
                        for retention in retention_str.split('\n'):
                            if retention:
                                value, unit = int(retention[:-1]), retention[-1]
                                if unit == 'd':
                                    retention_policy.append(f"RECOVERY WINDOW OF {value} DAYS")
                                elif unit == 'm':
                                    retention_policy.append(f"RECOVERY WINDOW OF {value} MONTHS")
                                elif unit == 'y':
                                    retention_policy.append(f"RECOVERY WINDOW OF {value} YEARS")
                        # Write the new retention policy to the file
                        config_file.write(f"retention_policy = {' AND '.join(retention_policy)}\n")

                return Response({'status': 'success', 'message': 'Retention period updated successfully.'}, status=200)
        return Response({'status': 'success', 'message': 'Updated successfully.'}, status=200)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_server_config(request):
    try:
        # Get server details from request parameters
        server_name = request.data.get('server_name')
        ssh_host = request.data.get('ssh_host')
        db_name = request.data.get('db_name')
        db_pass = request.data.get('db_pass')
        ssh_key = request.data.get('ssh_key')
        storage_method = request.data.get('storage_method')
        username = request.user

        if not (server_name, ssh_host, db_name, db_pass, ssh_key, storage_method):
            return Response({'status': 'error', 'message': 'All parameters are required.'}, status=400)

        # Construct the configuration file content
        config_content = f"""
[{server_name}]
description = "Configuration for {server_name} server"
ssh_command = ssh postgres@{ssh_host}
conninfo = host={ssh_host} user=barman dbname={db_name}
backup_method = rsync
archiver = on
backup_options = concurrent_backup
"""
        user_server_config = f"{CONFIG_DIR}/{username}/server_config/{storage_method}" 
        if not os.path.exists(user_server_config):
            try:
                mkdir_user_config_command = f"mkdir -p {user_server_config} && chmod 777 {user_server_config}"
                #mkdir_user_config_command = f"sudo mkdir -p {user_server_config} && sudo chmod 777 {user_server_config}"
                subprocess.run(mkdir_user_config_command, shell=True, check=True)
            except OSError as e:
                print(f"Error: {e.strerror}")
        # Write the configuration content to a new file
        config_file_path = os.path.join(user_server_config, f'{server_name}.conf') # /etc/barman.d/username/server_config/<storage_method>/<server_name>.conf
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_content)
    
        # Append the new entry to the .pgpass file
        with open(PGPASS_FILE, 'a') as pgpass_file:
            pgpass_file.write(f"{ssh_host}:5432:postgres:barman:{db_pass}\n")
        
        # Append public key 
        with open(AUTH_KEYS_FILE, 'a') as f:
            f.write(ssh_key + '\n')

        # Generating SSH Keys
        SSH_KEYGEN_COMMAND = f'ssh-keygen -f "/var/lib/barman/.ssh/known_hosts" -R "{ssh_host}"'
        try:
            subprocess.run(SSH_KEYGEN_COMMAND, shell=True, check=True)
        except:
            print(f"Error : Error while generating ssh keys for server {ssh_host}")



        return Response({'status': 'success', 'message': f'Configuration file created for {server_name}'}, status=200)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_nfs_mount(request):
    try:
        remote_host = request.query_params.get('remote_host')
        remote_path = request.query_params.get('remote_path')
        username = request.user

        if not all([remote_host, remote_path, username]):
            return JsonResponse({'status': 'error', 'message': 'All parameters are required.'}, status=400)

        local_path = f"/var/lib/barman/nfs/{username}"
        mkdir_command = f"mkdir -p {local_path}"    
        subprocess.run(mkdir_command, shell=True, check=True)

        # Add entry to /etc/fstab with sudo
        fstab_entry = f"{remote_host}:{remote_path} {local_path}    nfs defaults	0	0"
        fstab_command = f"echo '{fstab_entry}' | sudo tee -a /etc/fstab > /dev/null"
        subprocess.run(fstab_command, shell=True, check=True)
        
        # mount
        mount_nfs = "sudo mount -a"
        subprocess.run(mount_nfs, shell=True, check=True)
        subprocess.run(f"sudo chown barman:barman {local_path} -R", shell=True, check=True)

        # Create Barman Config file
        barman_user_config_dir = f"{CONFIG_DIR}/{username}"
        if not os.path.exists(barman_user_config_dir):
            try:
                mkdir_config_dir_command = f"mkdir -p {barman_user_config_dir}/server_config/nfs"
                #mkdir_config_dir_command = f"sudo mkdir -p {barman_user_config_dir}/server_config/nfs"
                subprocess.run(mkdir_config_dir_command, shell=True, check=True)
                #subprocess.run(f"sudo chmod 777 {barman_user_config_dir}", shell=True, check=True)
                subprocess.run(f"chmod 777 {barman_user_config_dir}", shell=True, check=True)
            except OSError as e:
                print(f"Error: {e.strerror}")

        barman_config_data = f"""barman_home = {local_path} \nconfiguration_files_directory = /etc/barman.d/{username}/server_config/nfs"""
        barman_config_command = f"echo '{barman_config_data}' | tee -a {barman_user_config_dir}/barman-nfs.conf > /dev/null"     
        #barman_config_command = f"echo '{barman_config_data}' | sudo tee -a {barman_user_config_dir}/barman-nfs.conf > /dev/null"     
        #copy_sample_config_command = f"sudo cp /etc/barman.conf.sample {barman_user_config_dir}/barman-nfs.conf"
        copy_sample_config_command = f"cp /etc/barman.conf.sample {barman_user_config_dir}/barman-nfs.conf"
        subprocess.run(copy_sample_config_command, shell=True, check=True)   
        subprocess.run(barman_config_command, shell=True, check=True)


        return JsonResponse({'message': 'NFS mount point {local_path} added successfully and entry added to /etc/fstab','status': 'success'}, status=200)
    except subprocess.CalledProcessError as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def mount_s3_bucket(request):
    try:
        bucket_name = request.query_params.get('bucket_name')
        access_key = request.query_params.get('access_key')
        secret_key = request.query_params.get('secret_key')
        url = request.query_params.get('url')
        username = request.user

        if not all([bucket_name, access_key, secret_key, url, username]):
            return JsonResponse({'status': 'error', 'message': 'All parameters are required.'}, status=400)

        local_path = f"/var/lib/barman/s3/{username}"
        mkdir_command = f"mkdir -p {local_path}"    
        subprocess.run(mkdir_command, shell=True, check=True)

        passwd_file_content = f"{access_key}:{secret_key}"
        passwd_file_path = f"{S3_CREDENTIALS_DIR}/.passwd-s3fs-{username}"

        # Write the .passwd-s3fs file
        with open(passwd_file_path, 'w') as f:
            f.write(passwd_file_content)

        # Change permission
        passwd_file_command = f"chmod 600 {passwd_file_path}"
        subprocess.run(passwd_file_command, shell=True, check=True)

        # Mount the bucket
        mount_command = f"s3fs {bucket_name} {local_path} -o passwd_file={passwd_file_path},use_path_request_style,url={url}"
        subprocess.run(mount_command, shell=True, check=True)

        # Create Barman Config file
        barman_user_config_dir = f"{CONFIG_DIR}/{username}"
        if not os.path.exists(barman_user_config_dir):
            try:
                mkdir_config_dir_command = f"mkdir -p {barman_user_config_dir}/server_config/s3"
                subprocess.run(mkdir_config_dir_command, shell=True, check=True)
                subprocess.run(f"chmod 777 {barman_user_config_dir}", shell=True, check=True)
                #subprocess.run(f"sudo chmod 777 {mkdir_config_dir_command}", shell=True, check=True)
            except OSError as e:
                print(f"Error: {e.strerror}")

        barman_config_data = f"""barman_home = {local_path} \nconfiguration_files_directory = /etc/barman.d/{username}/server_config/s3"""
        barman_config_command = f"echo '{barman_config_data}' | sudo tee -a {barman_user_config_dir}/barman-s3.conf > /dev/null"     
        #copy_sample_config_command = f"sudo cp /etc/barman.conf.sample {barman_user_config_dir}/barman-s3.conf"
        copy_sample_config_command = f"cp /etc/barman.conf.sample {barman_user_config_dir}/barman-s3.conf"
        subprocess.run(copy_sample_config_command, shell=True, check=True)   
        subprocess.run(barman_config_command, shell=True, check=True)


        return JsonResponse({'message': f'S3 bucket {bucket_name} mounted successfully','status': 'success'}, status=200)
    except subprocess.CalledProcessError as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_mount_points(request):
    try:
        username = request.user

        if not (username):
            return JsonResponse({'status': 'error', 'message': 'Invalid Username.'}, status=400)

        # Define the directories where mount points are located
        nfs_mount_points_dir = f'/var/lib/barman/nfs/{username}'
        s3_mount_points_dir = f'/var/lib/barman/s3/{username}'

        # Retrieve the list of NFS mount points from /etc/fstab
        nfs_mount_points = []
        with open('/etc/fstab', 'r') as fstab_file:
            for line in fstab_file:
                # Check if the line contains the user's NFS mount point
                if nfs_mount_points_dir in line:
                    # Extract host:path and mount point
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        host_path = parts[0]
                        mount_point = parts[1]
                        nfs_mount_points.append({'host_path': host_path, 'mount_point': mount_point})

        # Read the S3 credentials file
        s3_creds_file = f'/var/lib/barman/.s3-creds/.passwd-s3fs-{username}'
        s3_mount_points = []
        if os.path.exists(s3_creds_file):
            with open(s3_creds_file, 'r') as f:
                s3_creds = f.read().strip().split(':')
                access_key = s3_creds[0]
                secret_key = s3_creds[1]
                # Assuming the URL is common for all S3 mounts
                # s3_url = "https://s3.amazonaws.com"  # Replace this with your actual S3 URL
                s3_mount_points = [{'access_key': access_key, 'secret_key': secret_key, 'mount_point': s3_mount_points_dir}]

        return JsonResponse({'status': 'success', 'nfs_mount_points': nfs_mount_points, 's3_mount_points': s3_mount_points}, status=200)

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def unmount(request):
    try:
        username = request.user
        mount_type = request.query_params.get('storage_method')  # 'nfs' or 's3'

        if not (username, mount_type):
            return JsonResponse({'status': 'error', 'message': 'Invalid parameters.'}, status=400)

        # Define the mount directory based on the mount type
        mount_point = f"/var/lib/barman/{mount_type}/{username}"

        # Check if the mount point exists
        if not os.path.exists(mount_point):
            return Response({'status': 'error', 'message': 'Mount point not found.'}), 404

        # Unmount the specified mount point
        unmount_command = f'sudo umount {mount_point}'
        subprocess.run(unmount_command, shell=True, check=True)

        # Remove the mount point entry from /etc/fstab using sudo
        if mount_type == 'nfs':
            if remove_mount_point_from_fstab(mount_point):
                print(f"Mount point {mount_point} removed from /etc/fstab.")
            else:
                print("Failed to remove mount point.")

            if os.path.exists(mount_point):
                delete_user_dir_command = f"sudo rm -rf {mount_point}"
                subprocess.run(delete_user_dir_command, shell=True, check=True)
                print(f"Mount point {mount_point} empty directory deleted.")
            else:
                print("Failed to delete mount point.")

        if mount_type == 's3':        
            if os.path.exists(mount_point):
                delete_user_dir_command = f"sudo rm -rf {mount_point}"
                subprocess.run(delete_user_dir_command, shell=True, check=True)
                print(f"Mount point {mount_point} empty directory deleted.")
            else:
                print("Failed to delete mount point.")
        # Apply changes to /etc/fstab
        subprocess.run('sudo mount -a', shell=True, check=True)


        return JsonResponse({'status': 'success', 'message': f'{mount_point} unmounted successfully.'}, status=200)

    except subprocess.CalledProcessError as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_server(request):
    try:
        username = request.user
        storage_method = request.data.get('storage_method')  # 'nfs' or 's3'
        server_name = request.data.get('server_name')
 
        if not (username, storage_method, server_name):
            return Response({'status': 'error', 'message': 'Invalid parameters.'}, status=400)
        
        # Deleting data directory
        DATA_DIR = f"/var/lib/barman/{storage_method}/{username}/{server_name}"
        DATA_DIR_DEL_COMMAND = f"rm -rf {DATA_DIR}"
 
        if not os.path.exists(DATA_DIR):
            return Response({'status': 'error', 'message': f'{server_name}\'s data dir. not exists.'}, status=500)
 
        # Deleting configuration file
        CONFIG_DIR = "/etc/barman.d/"
        CONFIG_FILE = f"{CONFIG_DIR}/{username}/server_config/{storage_method}/{server_name}.conf"
        CONFIG_FILE_DEL_COMMAND = f"rm -f {CONFIG_FILE}"
 
        if not os.path.exists(CONFIG_FILE):
            return Response({'status': 'error', 'message': f'{server_name} server\'s configuration not exists.'}, status=500)
 
        subprocess.run(DATA_DIR_DEL_COMMAND, shell=True, check=True)
        subprocess.run(CONFIG_FILE_DEL_COMMAND, shell=True, check=True)
 
        return Response({'status': 'success', 'message': f'{server_name} deleted successfully.'}, status=200)
 
    except subprocess.CalledProcessError as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)
 
 
 