import os
from django.http import JsonResponse
from rest_framework import viewsets
from django.conf import settings
from userAuth_app.models import User
import ldap
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from userAuth_app.permissions import IsAllowedRole
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from provider1_api.models import Provider
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import subprocess
import json
import datetime
import subprocess
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import random
import string

@csrf_exempt
def kubectl_command(request):
    if request.method == 'POST':
        try:
            # Extracting the required fields from the POST data
            provider_name = request.data.get('provider')
            selected_key_name = request.data.get('selectedK8sKeyName')
            user_id = request.user.id  # Assuming you're using Django's built-in User model

            # Fetch the Provider instance matching the provider name, user ID, and selected key name
            provider = get_object_or_404(Provider, provider_name=provider_name, user_id=user_id, K8s_key_name=selected_key_name)
            
            # Retrieve the kubeconfig data from the Provider instance
            kubeconfig_data = provider.kubeconfig_data

            # Extract the command from the request data
            command = request.data.get('command')
            if not command:
                return HttpResponseBadRequest("No command provided")

            # Write kubeconfig data to a temporary file or use it directly depending on how kubectl is being invoked
            kubeconfig_path = "/path/to/kubeconfig/file"  # Define the path where you'll store kubeconfig data temporarily
            with open(kubeconfig_path, 'w') as f:
                f.write(kubeconfig_data)

            # Construct and execute the kubectl command using the kubeconfig
            command_list = ['kubectl', '--kubeconfig', kubeconfig_path] + command.split()

            result = subprocess.run(command_list, capture_output=True, text=True, check=True)
            return JsonResponse({'output': result.stdout, 'error': result.stderr})

        except subprocess.CalledProcessError as e:
            return JsonResponse({'output': e.stdout, 'error': e.stderr, 'returncode': e.returncode}, status=400)
    else:
        return HttpResponseNotAllowed(['POST'])

class FormViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAllowedRole]
    def create(self, request):
        ldap_server_uri = request.data.get('ldapServerURI')
        ldap_server_bind_on = request.data.get('ldapServerBIND_DN')
        ldap_server_bind_password = request.data.get('ldapServerBIND_PASSWORD')
        ldap_group_search = request.data.get('ldapGroupSearch')
        is_connected = request.data.get('True')
        try:
            # Read the contents of the settings.py file
            with open(settings.BASE_DIR / 'DBaas_project' / 'settings.py', 'r') as settings_file:
                lines = settings_file.readlines()
            # Write the lines back to the settings.py file, updating only the AUTH_LDAP_SERVER_URI variable
            with open(settings.BASE_DIR / 'DBaas_project' / 'settings.py', 'w') as settings_file:
                for line in lines:
                    if line.startswith('AUTH_LDAP_SERVER_URI'):
                        settings_file.write(f"AUTH_LDAP_SERVER_URI = '{ldap_server_uri}'\n")
                    elif line.startswith('AUTH_LDAP_BIND_DN'):
                        settings_file.write(f"AUTH_LDAP_BIND_DN = '{ldap_server_bind_on}'\n")
                    elif line.startswith('AUTH_LDAP_BIND_PASSWORD'):
                        settings_file.write(f"AUTH_LDAP_BIND_PASSWORD = '{ldap_server_bind_password}'\n")
                    elif line.startswith('ldapGroupSearch'):
                        settings_file.write(f"ldapGroupSearch = '{ldap_group_search}  '\n")
                    elif line.startswith('IS_CONNNECTED'):
                        settings_file.write(f"IS_CONNNECTED = '{is_connected}  '\n")
                    else:
                        settings_file.write(line)
                     # AUTH_LDAP_GROUP_SEARCH = LDAPSearch("CN=Users,DC=os3,DC=com", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
            return JsonResponse({'message': 'LDAP settings updated successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def reset_ldap_settings(request):
        try:
            # Update settings.py dynamically
            with open(os.path.join(settings.BASE_DIR, 'DBaas_project', 'settings.py'), 'a') as settings_file:
                settings_file.write("AUTH_LDAP_SERVER_URI = ''\n")
                settings_file.write("AUTH_LDAP_BIND_DN = ''\n")
                settings_file.write("AUTH_LDAP_BIND_PASSWORD = ''\n")
                settings_file.write("IS_CONNNECTED = ''\n")
            return JsonResponse({'message': 'LDAP settings disabled successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsAllowedRole])
def get_ad_users(request):
    try:
        # Establish LDAP connection
        ldap_server_uri = 'ldap://10.0.0.2:389'
        bind_dn = 'CN=Administrator,CN=Users,DC=os3,DC=com'
        bind_password = 'P@33w0rd'
        ldap_connection = ldap.initialize(ldap_server_uri)
        ldap_connection.simple_bind_s(bind_dn, bind_password)
        search_base = 'CN=Users,DC=os3,DC=com'
        search_filter = "(sAMAccountName=*)"  # Filter to retrieve all users
        ldap_users = ldap_connection.search_s(
            search_base,
            ldap.SCOPE_SUBTREE,
            search_filter,
            ['sAMAccountName']
        )
        # Extract usernames
        user_names = [entry.get('sAMAccountName', [])[0].decode('utf-8') for dn, entry in ldap_users]
        return JsonResponse({'user_names': user_names}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class CreateServerConfigView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Assuming IsAllowedRole is your custom permission

    def generate_random_password(self, length=12):
        """Generate a random strong password."""
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def post(self, request):
        # Get the data from POST request
        data = request.data  # Use request.data for JSON payload
        
        # Get the email of the logged-in user
        user_email = request.user.email  # Get the email from the logged-in user

        # Command to check if the user exists in pgAdmin
        check_command = [
            '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/bin/python3',
            '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/lib/python3.8/site-packages/pgadmin4/setup.py',
            'get-users'
        ]

        user_exists = False
        random_password = None  # Initialize variable for random password

        try:
            # Execute the command to get user details
            result = subprocess.run(check_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode('utf-8')

            # Check if the user's email is present in the output
            if user_email in output:
                user_exists = True
            else:
                # Generate a random password
                random_password = self.generate_random_password()
                
                # Command to add a new user
                add_user_command = [
                    '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/bin/python3',
                    '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/lib/python3.8/site-packages/pgadmin4/setup.py',
                    'add-user',
                    user_email,
                    random_password,
                    '--nonadmin',
                    '--active'
                ]

                # Execute the command to add the user
                subprocess.run(add_user_command, check=True)  # check=True will raise an error for non-zero exit codes

        except subprocess.CalledProcessError as e:
            return JsonResponse({"error": f"Error checking or creating user in pgAdmin4: {str(e)}"}, status=500)

        # Create a Python dictionary structure for the JSON file
        server_data = {
            "Servers": {
                "1": {
                    "Name": data.get("Name"),
                    "Group": data.get("Group"),
                    "Host": data.get("Host"),
                    "Port": int(data.get("Port")),
                    "Username": data.get("Username"),
                    "SSLMode": data.get("SSLMode"),
                    "MaintenanceDB": data.get("MaintenanceDB")
                }
            }
        }

        # Convert the dictionary to JSON format
        json_data = json.dumps(server_data, indent=4)
        
        # Define the file path, appending a timestamp to the filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"servers_{timestamp}.json"
        file_path = os.path.join('/home/ubuntu/stable-code/bitblast-application/JSON_FILES', file_name)

        # Make sure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write the JSON data to a new file with the unique name
        with open(file_path, 'w') as json_file:
            json_file.write(json_data)

        # Command to run after creating the file
        command = [
            '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/bin/python3',
            '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/lib/python3.8/site-packages/pgadmin4/setup.py',
            'load-servers',
            file_path,
            '--user',
            user_email  # Use the email of the logged-in user here
        ]

        # Execute the command
        try:
            subprocess.run(command, check=True)  # check=True will raise an error for non-zero exit codes
        except subprocess.CalledProcessError as e:
            return JsonResponse({"error": str(e)}, status=500)

        # Create the response JSON object
        response_data = {
            "message": "Server configuration loaded successfully.",
            "file_path": file_path,
            "user_email": user_email
        }

        # If a new user was created, add the password to the response
        if random_password:
            response_data["new_user"] = {
                "email": user_email,
                "password": random_password
            }

        # Return a success response with the file path and optionally the user password
        return JsonResponse(response_data, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class RemoveServerConfigView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Assuming IsAllowedRole is your custom permission

    def post(self, request):
        # Get the server name from the request data
        data = request.data
        server_name = data.get('server_name')

        if not server_name:
            return JsonResponse({"error": "Server name is required."}, status=400)

        # Get the email of the logged-in user
        user_email = request.user.email  # Get the email from the logged-in user

        # Command to remove the server from pgAdmin for the user
        remove_command = [
            '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/bin/python3',
            '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/lib/python3.8/site-packages/pgadmin4/setup.py',
            'remove-server',
            server_name,
            '--user',
            user_email  # Use the logged-in user's email
        ]

        try:
            # Execute the command to remove the server
            subprocess.run(remove_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Now check and delete the corresponding JSON file
            json_folder_path = '/home/ubuntu/stable-code/bitblast-application/JSON_FILES'
            found_file = None

            # Loop through JSON files to find the one that contains the server
            for file_name in os.listdir(json_folder_path):
                file_path = os.path.join(json_folder_path, file_name)
                if file_name.endswith('.json'):
                    with open(file_path, 'r') as json_file:
                        file_data = json.load(json_file)
                        if server_name in json.dumps(file_data):  # Check if server name exists in the file
                            found_file = file_path
                            break  # Exit the loop once the file is found

            if found_file:
                os.remove(found_file)  # Delete the JSON file containing the server details
                return JsonResponse({"message": f"Server '{server_name}' removed successfully and JSON file deleted."}, status=200)
            else:
                return JsonResponse({"message": f"Server '{server_name}' removed but no associated JSON file found."}, status=200)

        except subprocess.CalledProcessError as e:
            return JsonResponse({"error": f"Error removing server '{server_name}': {str(e)}"}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class CreatePgAdminUserView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get email, password, and is_admin flag from the request body
        user_email = request.data.get("email")
        password = request.data.get("password")
        is_admin = request.data.get("is_admin", False)  # Default to non-admin if not provided

        # Check if email and password are provided
        if not user_email or not password:
            return JsonResponse({"error": "Email and password are required."}, status=400)

        # Validate password length (must be at least 6 characters)
        if len(password) < 6:
            return JsonResponse({"error": "Password must be at least 6 characters long."}, status=400)

        # Define the base command to add the user to pgAdmin
        add_user_command = [
            '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/bin/python3',
            '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/lib/python3.8/site-packages/pgadmin4/setup.py',
            'add-user',
            user_email,
            password,
            '--active'
        ]

        # Append the admin or non-admin flag based on the is_admin value
        if is_admin:
            add_user_command.append('--admin')
        else:
            add_user_command.append('--nonadmin')

        try:
            # Execute the command
            subprocess.run(add_user_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Return a success response with the created user's email
            user_type = "Admin" if is_admin else "Non-admin"
            return JsonResponse({
                "message": f"{user_type} user created successfully in pgAdmin.",
                "email": user_email
            }, status=201)

        except subprocess.CalledProcessError as e:
            # Handle command failure
            return JsonResponse({
                "error": f"Error creating user in pgAdmin: {e.stderr.decode('utf-8')}"
            }, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class UpdatePgAdminUserStatusView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_email = request.data.get("email")
        is_active = request.data.get("is_active")
        new_password = request.data.get("password")

        if not user_email:
            return JsonResponse({"error": "Email is required."}, status=400)

        if new_password:
            if len(new_password) < 6:
                return JsonResponse({"error": "Password must be at least 6 characters long."}, status=400)

        # Define the command for updating the user status or password
        update_command = [
            '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/bin/python3',
            '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/lib/python3.8/site-packages/pgadmin4/setup.py',
            'update-user',
            user_email
        ]

        # Add the password change option if provided
        if new_password:
            update_command.append('--password')
            update_command.append(new_password)

        # Add the active status change option if provided
        if is_active is not None:
            if is_active:
                update_command.append('--active')
            else:
                update_command.append('--inactive')

        try:
            # Execute the command
            subprocess.run(update_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            return JsonResponse({
                "message": "User status and/or password updated successfully in pgAdmin.",
                "email": user_email
            }, status=200)

        except subprocess.CalledProcessError as e:
            return JsonResponse({
                "error": f"Error updating user in pgAdmin: {e.stderr.decode('utf-8')}"
            }, status=500)






