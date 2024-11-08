from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Project, Cluster, Db_credentials, Db_credentials, Cluster_History
from .serializers import projectSerializers, ClusterSerializers,ClusterHistorySerializers
from django.shortcuts import render
from rest_framework.response import Response
from userAuth_app.models import User
from rest_framework.decorators import api_view
import requests
import zipfile
import io
from django.http import JsonResponse
import time
import logging
import os
from dotenv import load_dotenv
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from userAuth_app.permissions import IsAllowedRole
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
import subprocess
from provider1_api.models import Provider
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
import urllib
import base64
import urllib.parse
import urllib.request
import json
import hashlib
import hmac
from rest_framework import generics
from kubernetes import client, config
import tempfile
import re

from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import subprocess



import json
import os
import datetime
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import random
import string


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


load_dotenv() 
 
project_logger = logging.getLogger('project_logger')
rename_project_logger = logging.getLogger('rename_project_logger')

class ProjectViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]   
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = projectSerializers

    def create(self, request, *args, **kwargs):
        user = request.user
        project_name = request.data.get('project_name')

        project_logger.debug(f"Received create request from user={user.username} with project_name={project_name}")

        if not user:
            project_logger.error("User is required but not found in request")
            return Response({"error": "User is required"}, status=status.HTTP_400_BAD_REQUEST)

        if not project_name:            
            project_logger.error("Project name is required but not found in request")
            return Response({"error": "Project name is required"}, status=status.HTTP_400_BAD_REQUEST)   

        existing_project = Project.objects.filter(project_name=project_name).exists()

        if existing_project:
            project_logger.error(f"Project with name {project_name} already exists")
            return Response({"error": "Project already exists"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            project = Project.objects.create(user=user, project_name=project_name)
            project.save()

            log_entry = f"user={user.username} projectName={project.project_name} msg={project.project_name} created"
            project_logger.info(log_entry)

            serializer = self.get_serializer(project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            project_logger.error(f"Error creating project: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
    @action(detail=True, methods=['PUT'], url_path='rename')
    def rename_project(self, request, pk=None):
        # permission_classes = [IsAllowedRole]
        project = self.get_object()
        new_project_name = request.data.get('new_project_name')
 
        if not new_project_name:
            return Response({
                "error": "new_project_name is required"
            }, status=status.HTTP_400_BAD_REQUEST)
 
        existing_project = Project.objects.exclude(pk=project.id).filter(project_name=new_project_name).exists()
 
        if existing_project:
            return Response({
                "error": "Project with the new name already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
      
 
        project.project_name = new_project_name
        project.save()
 
        log_entry_after_rename = f"user={project.user.username} projectname={project.project_name} msg={ project.project_name } renamed"
        rename_project_logger.info(log_entry_after_rename)
 
        serializer = projectSerializers(project)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    rename_project.permission_classes = [IsAllowedRole]    

    
class ComputeOfferingsAPIView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]
  
    def get(self, request):
        
        baseurl = os.getenv('BASEURL')

        request_data = {
                'command': 'listServiceOfferings',
                'response': 'json',
                'apikey': os.getenv('API_KEY')
        }
        secret_key = os.getenv('SECRET_KEY_ENCODED').encode('utf-8')

 
        request_str = '&'.join(['='.join([k, urllib.parse.quote_plus(request_data[k])]) for k in request_data.keys()])
 
        sig_str = '&'.join(['='.join([k.lower(), urllib.parse.quote_plus(request_data[k]).lower().replace('+', '%20')])
                            for k in sorted(request_data.keys())])
 
        sig = urllib.parse.quote_plus(
            base64.b64encode(hmac.new(secret_key, sig_str.encode('utf-8'), hashlib.sha1).digest()).
            strip())
 
        req = baseurl + request_str + '&signature=' + sig
 
        try:
            res = urllib.request.urlopen(req)
            response_data = json.loads(res.read().decode('utf-8'))
 
            if 'listserviceofferingsresponse' in response_data:
                service_offerings = response_data['listserviceofferingsresponse'].get('serviceoffering', [])
 
                # Create a list to store compute offerings
                compute_offerings = []
 
                # Add data to the list
                for offering in service_offerings:
                    compute_offerings.append({
                        'name': offering['name'],
                        'cpunumber': offering['cpunumber'],
                        'cpuspeed': offering['cpuspeed'],
                        'memory': offering['memory']
                    })
 
                return Response({'compute_offerings': compute_offerings})
            else:
                error_message = "Error: Unable to fetch compute offerings."
        except Exception as e:
            error_message = f"Error: {str(e)}"
 
        return Response({'error': error_message}, status=500)   

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_storage_classes(request):
    try:
        api_url = request.data.get('api_url')
        username = request.data.get('OpenShift_username')
        password = request.data.get('OpenShift_password')
        print("Received data:", api_url, username, password)
        def oc_login(api_url, username, password):
            try:
                subprocess.run(
                    ["oc", "login", api_url, "-u", username, "-p", password, "--insecure-skip-tls-verify"],
                    check=True,
                    capture_output=True
                )
                
            except subprocess.CalledProcessError as e:
                print(f"Failed to login to OpenShift: {e.stderr.decode()}")
                return False
            return True
        def get_storage_classes():
            try:
                result = subprocess.run(
                    ["oc", "get", "storageclass", "-o", "json"],
                    check=True,
                    capture_output=True
                )
                storage_classes = json.loads(result.stdout.decode())
                return storage_classes['items']
            except subprocess.CalledProcessError as e:
                print(f"Error retrieving StorageClasses: {e.stderr.decode()}")
                return []
        if oc_login(api_url, username, password):
            storage_classes = get_storage_classes()
            response_data = [{'name': sc['metadata']['name']} for sc in storage_classes]
            return JsonResponse(response_data, safe=False)
        else:
            return JsonResponse({'error': 'Failed to login to OpenShift'}, status=500)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return JsonResponse({'error': 'An unexpected error occurred'}, status=500)



@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def K8s_storage_classes(request):
    try:
        provider_name = 'Kubernetes'
        
        # Parse JSON data from the request body
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)

        selected_k8s_key_name = data.get('selectedK8sKeyName')

        if not selected_k8s_key_name:
            return JsonResponse({"error": "No Kubernetes key name provided."}, status=400)

        k8s_providers = Provider.objects.filter(K8s_key_name=selected_k8s_key_name, provider_name=provider_name)

        if not k8s_providers.exists():
            return JsonResponse({"error": "No matching Kubernetes provider found."}, status=404)

        if k8s_providers.count() > 1:
            return JsonResponse({"error": "Multiple providers found. Please refine your search."}, status=400)

        k8s_provider = k8s_providers.first()
        kubeconfig_data = k8s_provider.kubeconfig_data

        with tempfile.NamedTemporaryFile(delete=False) as temp_config_file:
            temp_config_file.write(kubeconfig_data.encode())
            temp_config_file_name = temp_config_file.name
            temp_config_file.close()

        try:
            config.load_kube_config(config_file=temp_config_file_name)
            storage_v1_api = client.StorageV1Api()
            storage_classes = storage_v1_api.list_storage_class()

            storage_class_list = []
            for sc in storage_classes.items:
                storage_class_list.append({
                    "name": sc.metadata.name,
                    "provisioner": sc.provisioner,
                    "reclaim_policy": sc.reclaim_policy,
                    "volume_binding_mode": sc.volume_binding_mode,
                    "allow_volume_expansion": sc.allow_volume_expansion,
                    "creation_timestamp": sc.metadata.creation_timestamp,
                })

            return JsonResponse({"storage_classes": storage_class_list})

        finally:
            if os.path.exists(temp_config_file_name):
                os.remove(temp_config_file_name)

    except Provider.DoesNotExist:
        return JsonResponse({"error": "Provider not found."}, status=404)
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return JsonResponse({"error": str(e)}, status=500)


from rest_framework.views import APIView
from rest_framework.response import Response
import openstack
 
class FlavorList(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Retrieve flavors from OpenStack
        conn = openstack.connect(
            auth_url = os.getenv('AUTH_URL'),
            project_name = os.getenv('PROJECT_NAME'),
            username = os.getenv('USERNAME'),
            password = os.getenv('PASSWORD'),
            user_domain_name = os.getenv('USER_DOMAIN_NAME'),
            project_domain_name = os.getenv('PROJECT_DOMAIN_NAME')

        )
        flavors = conn.compute.flavors()
 
        # Transform flavors data into a list of dictionaries
        flavor_data = [

            
            {
                'flavors': {'flavor_id': flavor.id, 'name': flavor.name},
              
                'ram': flavor.ram,
                'vcpus': flavor.vcpus,
                'disk': flavor.disk,
                'is_public': flavor.is_public
            }
            for flavor in flavors
        ]
 
        # Return flavors data as JSON response
        return Response(flavor_data)
 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_projects_by_user(request):
    # Get the authenticated user
    user = request.user

    # Fetch projects for the authenticated user
    projects = Project.objects.filter(user=user)
    serializer = projectSerializers(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])

def get_projects_by_username(request):

    # Get the authenticated user

    username = request.query_params.get('username')

    user = User.objects.get(username=username)
 
    # Fetch projects for the authenticated user

    projects = Project.objects.filter(user=user)

    serializer = projectSerializers(projects, many=True)

    return Response(serializer.data)

 

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_projects_by_user_one(request):
    # Get the authenticated user
    user = request.user
    # Fetch projects for the authenticated user
    projects = Project.objects.filter(user=user)
    # Pagination
    paginator = CustomPagination()
    result_page = paginator.paginate_queryset(projects, request)
    serializer = projectSerializers(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

 

class ClusterViewSet2(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializers
    pagination_class = CustomPagination

class ProjectViewSet2(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]   
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = projectSerializers
    pagination_class = CustomPagination


from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


# Define a logger for cluster-related actions
cluster_logger = logging.getLogger('cluster_logger')
class ClusterViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializers
 
    def create(self, request, *args, **kwargs):
        global pipeline_dict
      
        username = request.data.get('db_user')
        password = request.data.get('db_password')
        user_id = request.user.id
        project_id = request.data.get('project')
        print("project_id 1 : ", project_id)
        cluster_name = request.data.get('cluster_name')
        cluster_type = request.data.get('cluster_type')
        database_version = request.data.get('postgres_version')
        backup_method = request.data.get('backup_method')
        storage_class = request.data.get('storageClass')
        size = request.data.get('size')
        flavor_id = request.data.get('flavor_id')
        k8sClass = request.data.get('k8sClass')
        osType = request.data.get('osType')
        airgap = request.data.get('airgap')
        pg_db_name = request.data.get('pg_db_name')
        pg_grp_name = request.data.get('pg_grp_name')
        pg_ha_grp_name = request.data.get('pg_ha_grp_name')
        is_pgadmin4 = request.data.get('is_pgadmin4', False) # Retrieve the is_pgadmin4 value, default to False if not provided
        print("is_pgadmin4 boolean value : " , is_pgadmin4)

        

        user_token = Token.objects.get(user=request.user).key
        provider_name = request.data.get('provider')
        selected_key_name = request.data.get('selectedK8sKeyName')
        # print("selected key name : ", selected_key_name)
        provider = get_object_or_404(Provider, provider_name=provider_name, user_id=user_id, K8s_key_name=selected_key_name)
        kubeconfig_data = provider.kubeconfig_data

        provider_endpoint = provider.provider_url
        provider_access_token = provider.access_token
        provider_secret_key = provider.secret_key
        openstackusername = provider.openStackuser
        tenant_name = provider.tenant_name
        openstackpassword= provider.openstackpassword
        auth_url = provider.auth_url
        region = provider.region
        OpenShift_username = provider.OpenShift_username
        OpenShift_password = provider.OpenShift_password
        api_url = provider.api_url
  
  
        computeOffering  = request.data.get('computeOffering')
        storageOffering = request.data.get('storageOffering')
        mount_point = request.data.get('mount_point')
       
       
        user = User.objects.get(pk=user_id)
              
        # Check if cluster with the same name already exists in the project
        existing_cluster = Cluster.objects.filter(project=project_id, cluster_name=cluster_name).exists()
 
        if existing_cluster:
            return Response({"error": "Cluster with the same name already exists in the project"}, status=status.HTTP_400_BAD_REQUEST)
 
        try:
            user = User.objects.get(pk=user_id)
            project = Project.objects.get(pk=project_id)
 
        except User.DoesNotExist:
            return Response({"error": "User with the provided ID does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Project.DoesNotExist:
            return Response({"error": "No Project! has been selected.."}, status=status.HTTP_404_NOT_FOUND)
            

        project_id_gitlab = os.getenv('PROJECT_ID')
        private_token = os.getenv('PRIVATE_TOKEN')
        base_url = os.getenv('BASE_URL')

        headers = {"PRIVATE-TOKEN": private_token}
        
        if provider_name == 'Kubernetes' and cluster_type == 'Standalone':
            formData = {
                "ref": 'rke2-standalone',
                "variables": [
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "KUBE_CONFIG", "value": kubeconfig_data},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "USERNAME", "value": username}, 
                {"key": "PASSWORD", "value": password},
                {"key": "STORAGE_CLASS", "value": k8sClass}, 
                {"key": "SIZE", "value": size},           
           
             ]
            }
            response = trigger_single(base_url, project_id_gitlab, headers, user_id, formData)
            print("response :", response )
            pipeline_id = response[1]
            if response[0] == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method="StorageClass/"+k8sClass,
                    provider=provider_name,  
                    k8s_key_name=selected_key_name  # Save the selected key name

                )
                cluster.save()
                # Get and save artifacts
                print(f"pipeline_id and user_id = {pipeline_id} {user_id}")

                artifacts = get_latest_pipeline_artifacts(base_url, project_id_gitlab, headers, pipeline_id, cluster_name, cluster_type, database_version, provider_name, user_id,  project)
                print("New Artifacts:", artifacts)  # Print the artifacts
                cluster.artifacts = artifacts
               
                serializer = ClusterSerializers(cluster)
                time.sleep(6)
                pipeline_dict[user_id].remove(pipeline_id)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
              
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:  
                # Cluster creation failed
                print("cluster history")
                Cluster_History.objects.create(
                    userID=user,
                    clustername=cluster_name,
                    cluster_status='failed'
                ) 
                time.sleep(6)
                pipeline_dict[user_id].remove(pipeline_id)          
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  
        
        elif provider_name == 'Kubernetes' and cluster_type == 'Multiple':
            formData = {
                "ref": 'rke2-ha',
                "variables": [
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "KUBE_CONFIG", "value": kubeconfig_data},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "USERNAME", "value": username}, 
                {"key": "PASSWORD", "value": password},
                {"key": "STORAGE_CLASS", "value": k8sClass}, 
                {"key": "SIZE", "value": size},                      
             ]
            }
            response = trigger_single(base_url, project_id_gitlab, headers, user_id, formData)
            print("response :", response )
            pipeline_id = response[1]
            if response[0] == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method="StorageClass/"+k8sClass,
                    provider=provider_name,  
                    k8s_key_name=selected_key_name  # Save the selected key name
                )               
                cluster.save()
                # Get and save artifacts
                # pipeline_id = response[1]
                print(f"pipeline_id and user_id = {pipeline_id} {user_id}")
                artifacts = get_latest_pipeline_artifacts(base_url, project_id_gitlab, headers, pipeline_id, cluster_name, cluster_type, database_version, provider_name, user_id,  project)
                print("New Artifacts:", artifacts)  # Print the artifacts
                

                serializer = ClusterSerializers(cluster)
                time.sleep(6)
                pipeline_dict[user_id].remove(pipeline_id)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else: 
                # Cluster creation failed
                Cluster_History.objects.create(
                    userID=user,
                    clustername=cluster_name,
                    cluster_status='failed'
                )  
                time.sleep(6)
                pipeline_dict[user_id].remove(pipeline_id)          
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
        
        elif provider_name == 'CloudStack' and cluster_type == 'Multiple':
            is_pgadmin = request.data.get("isPgAdmin", False)  # Get isPgAdmin from the request data
            print("is_pgadmin:" , is_pgadmin)
            formData = {
                "ref": 'cloudstack-ha',
                "variables": [
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "PROVIDER_ENDPOINT", "value": provider_endpoint},
                {"key": "PROVIDER_SECRET_KEY", "value": provider_secret_key},
                {"key": "PROVIDER_ACCESS_KEY", "value": provider_access_token},
                {"key": "COMPUTE_OFFERING", "value": computeOffering},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "STORAGE_OFFERING", "value": storageOffering},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "USERNAME", "value": username}, 
                {"key": "PASSWORD", "value": password},
                {"key": "OS_TYPE", "value": osType},  
                {"key": "AIRGAP_INS", "value": airgap},
                {"key": "TOKEN", "value": user_token},
                {"key": "PG_HA_GRP_NAME", "value": pg_ha_grp_name},             
             ]
            }
            response = trigger_single(base_url, project_id_gitlab, headers, user_id,formData )

            print("CloudStack HA branch trigger.....")
            pipeline_id = response[1]
            if response[0] == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method=backup_method,
                    provider=provider_name,
                    is_pgadmin4=is_pgadmin4 # save the is_pgadmin4 value in the   cluster                 

                )
                cluster.save()
                # Get and save artifacts
                # pipeline_id = response[1]
                print(f"pipeline_id and user_id = {pipeline_id} {user_id}")
                artifacts = get_latest_pipeline_artifacts(base_url, project_id_gitlab, headers, pipeline_id, cluster_name, cluster_type, database_version, provider_name, user_id,  project)
                print("New Artifacts:", artifacts)  # Print the artifacts
                
                
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)


                if is_pgadmin:
                    artifacts = get_latest_pipeline_artifacts(base_url, project_id_gitlab, headers, pipeline_id, cluster_name, cluster_type, database_version, provider_name, user_id, project)  
                    if artifacts:
                        content = artifacts[0]['content']  # Extract the 'content' field from the first artifact
                        
                        # Use regex to extract the host, port, username, and password from the connection string
                        connection_string_match = re.search(r'postgres:\/\/(\S+):(\S+)@(\S+):(\d+)\/postgres', content)
                        
                        if connection_string_match:
                            username = connection_string_match.group(1)  # Extract username
                            host = connection_string_match.group(3)      # Extract host
                            port = connection_string_match.group(4)      # Extract port


                        # Creating JSON file for the server information
                        cluster_name = next((item['value'] for item in formData['variables'] if item['key'] == 'DATABASE_NAME'), None)
                        pg_ha_grp_name = next((item['value'] for item in formData['variables'] if item['key'] == 'PG_HA_GRP_NAME'), None)

                        # Creating JSON file for the server information
                        server_data = {
                            "Servers": {
                                "1": {
                                    "Name": cluster_name,  # Fetching PG_DB_NAME from formData
                                    "Group": pg_ha_grp_name,  # Fetching PG_GRP_NAME from formData
                                    "Host": host,  # using the extracted Host from artifacts
                                    "Port": int(port),  # using the extracted Port from artifacts
                                    "Username": username,  # using the extracted Database User
                                    "SSLMode": "prefer",
                                    "MaintenanceDB": "postgres"
                                }
                            }
                        }
                        print("server_data :" , server_data)

                        pg_dashboard(request,server_data)
              

                serializer = ClusterSerializers(cluster)
                
                time.sleep(6)
                pipeline_dict[user_id].remove(pipeline_id)
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                    
            else:   
                # Cluster creation failed
                Cluster_History.objects.create(
                    userID=user,
                    clustername=cluster_name,
                    cluster_status='failed'
                ) 
                time.sleep(6)  
                pipeline_dict[user_id].remove(pipeline_id)       
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        elif provider_name == 'Harvester' and cluster_type == 'Standalone':
            print("harvesr ha branch trigger.....")

            response = trigger_single(base_url, project_id_gitlab, headers, user_id, 'Harvester')
            pipeline_id = response[1]
            if response[0] == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method=backup_method,

                    provider=provider_name
                )
                cluster.save()

                # Get and save artifacts
                pipeline_id = response[1]
                artifacts = get_latest_pipeline_artifacts(base_url, project_id_gitlab, headers, pipeline_id, cluster_name, cluster_type, database_version, provider_name, user_id,  project)
                print("New Artifacts:", artifacts)  # Print the artifacts
                cluster.artifacts = artifacts

                serializer = ClusterSerializers(cluster)
                time.sleep(6)
                pipeline_dict[user_id].remove(pipeline_id)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                    
            else:  
                # Cluster creation failed
                Cluster_History.objects.create(
                    userID=user,
                    clustername=cluster_name,
                    cluster_status='failed'
                )           
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
        elif provider_name == 'CloudStack' and cluster_type == 'Standalone':
            is_pgadmin = request.data.get("isPgAdmin", False)  # Get isPgAdmin from the request data
            print("is_pgadmin:" , is_pgadmin)
            barman_ip = "172.16.1.190"
            bitblast_ip = "172.16.1.190"
            print(bitblast_ip)
            formData = {
                "ref": 'cloudstack-standalone',
                "variables": [
                {"key": "BITBLAST_USERNAME", "value": user.username},
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "PROVIDER_ENDPOINT", "value": provider_endpoint},
                {"key": "PROVIDER_SECRET_KEY", "value": provider_secret_key},
                {"key": "PROVIDER_ACCESS_KEY", "value": provider_access_token},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "MOUNT_POINT", "value": mount_point},
                {"key": "BARMAN_SERVER", "value":barman_ip},
                {"key": "BITBLAST_IP", "value": bitblast_ip},
                {"key": "COMPUTE_OFFERING", "value": computeOffering},
                {"key": "STORAGE_OFFERING", "value": storageOffering},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "USERNAME", "value": username},
                {"key": "PASSWORD", "value": password},
                {"key": "OS_TYPE", "value": osType},  
                {"key": "AIRGAP_INS", "value": airgap},
                {"key": "TOKEN", "value": user_token},
                {"key": "PG_GRP_NAME", "value": pg_grp_name},          
             ]
            }
            print("formdata",formData)
            response = trigger_single(base_url, project_id_gitlab, headers, user_id,formData)
            print("CloudStack branch trigger.....")
            pipeline_id = response[1]
            if response[0] == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method=backup_method,
                    provider=provider_name, 
                    is_pgadmin4=is_pgadmin4 # save the is_pgadmin4 value in the   cluster                 
                  
                )
                
                cluster.save()
                # Get and save artifacts
                artifacts = get_latest_pipeline_artifacts(base_url, project_id_gitlab, headers, pipeline_id, cluster_name, cluster_type, database_version, provider_name, user_id,  project)

                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                              
                # Only execute pgAdmin code if is_pgadmin is True
                if is_pgadmin:
                    artifacts = get_latest_pipeline_artifacts(base_url, project_id_gitlab, headers, pipeline_id, cluster_name, cluster_type, database_version, provider_name, user_id, project)
                    if artifacts:
                        content = artifacts[0]['content']
                        database_user = re.search(r'Database User:\s*(\S+)', content).group(1)
                        host = re.search(r'Host:\s*(\S+)', content).group(1)
                        port = re.search(r'Port:\s*(\S+)', content).group(1)
                        password = re.search(r'Password:\s*(\S+)', content).group(1)

                        # Creating JSON file for the server information
                        cluster_name = next((item['value'] for item in formData['variables'] if item['key'] == 'DATABASE_NAME'), None)
                        pg_grp_name = next((item['value'] for item in formData['variables'] if item['key'] == 'PG_GRP_NAME'), None)

                        # Construct server data for pgAdmin
                        server_data = {
                            "Servers": {
                                "1": {
                                    "Name": cluster_name,
                                    "Group": pg_grp_name,
                                    "Host": host,
                                    "Port": int(port),
                                    "Username": database_user,
                                    "SSLMode": "prefer",
                                    "MaintenanceDB": "postgres"
                                }
                            }
                        }
                        print("server_data :" , server_data)
                        pg_dashboard(request, server_data)
                
                serializer = ClusterSerializers(cluster)
                
                time.sleep(6)
                pipeline_dict[user_id].remove(pipeline_id)

                                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:  
                # Cluster creation failed
                Cluster_History.objects.create(
                    userID=user,
                    clustername=cluster_name,
                    cluster_status='failed'
                ) 
                time.sleep(6)
                pipeline_dict[user_id].remove(pipeline_id)          
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
        elif provider_name == 'OpenStack' and cluster_type == 'Standalone':
            formData = {
                "ref": 'openstack-standalone',
                "variables": [
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "OPENSTACK_USER", "value": openstackusername},
                {"key": "OPENSTACK_PASSWORD", "value":  openstackpassword},
                {"key": "TENANT_NAME", "value": tenant_name}, 
                {"key": "REGION", "value": region}, 
                {"key": "AUTH_URL", "value": auth_url},
                {"key": "OS_FLAVOR_ID", "value": flavor_id},
                {"key": "OS_TYPE", "value": osType}, 
                {"key": "AIRGAP_INS", "value": airgap},           
             ]
            }
            response = trigger_single(base_url, project_id_gitlab, headers, user_id, formData)
            print("Openstack Standalone branch trigger.....")
            if response == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method=backup_method,
                    provider=provider_name,
                    
                )
                cluster.save()

                # Get and save artifacts
                pipeline_id = pipeline_dict.get(user_id)[0]
                print("pipeline_id ni :", pipeline_id)
                artifacts = get_latest_pipeline_artifacts(base_url, project_id_gitlab, headers, pipeline_id, cluster_name, cluster_type, database_version, provider_name, user_id,  project)
                print("New Artifacts:", artifacts)  # Print the artifacts
                cluster.artifacts = artifacts

                serializer = ClusterSerializers(cluster)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:   
                # Cluster creation failed
                Cluster_History.objects.create(
                    userID=user,
                    clustername=cluster_name,
                    cluster_status='failed'
                )          
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        elif provider_name == 'OpenStack' and cluster_type == 'Multiple':
            formData = {
                "ref": 'openstack-provider-ha-vip',
                "variables": [
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "OPENSTACK_USER", "value": openstackusername},
                {"key": "OPENSTACK_PASSWORD", "value":  openstackpassword},
                {"key": "TENANT_NAME", "value": tenant_name}, 
                {"key": "REGION", "value": region}, 
                {"key": "AUTH_URL", "value": auth_url}, 
                {"key": "OS_FLAVOR_ID", "value": flavor_id},
                {"key": "OS_TYPE", "value": osType},  
                {"key": "AIRGAP_INS", "value": airgap},            
          
             ]
            }
            response = trigger_single(base_url, project_id_gitlab, headers, user_id, formData)
            print("Openstack HA branch trigger.....")
            if response == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method=backup_method,
                    provider=provider_name,
                    
                )
                cluster.save()

                # Get and save artifacts
                pipeline_id = pipeline_dict.get(user_id)[0]
                print("pipeline_id :", pipeline_id)
                artifacts = get_latest_pipeline_artifacts(base_url, project_id_gitlab, headers, pipeline_id, cluster_name, cluster_type, database_version, provider_name, user_id,  project)
                print("New Artifacts:", artifacts)  # Print the artifacts
                cluster.artifacts = artifacts

                serializer = ClusterSerializers(cluster)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:   
                # Cluster creation failed
                Cluster_History.objects.create(
                    userID=user,
                    clustername=cluster_name,
                    cluster_status='failed'
                )          
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        elif provider_name == 'OpenShift' and cluster_type == 'Standalone':
            print("openshift provider")
            formData = {
                "ref": 'openshift-standalone',
                # "ref": 'ankitv-test',
                "variables": [
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "OPN_USERNAME", "value": OpenShift_username},
                {"key": "OPN_PASSWORD", "value": OpenShift_password},
                {"key": "API_URL", "value": api_url},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "USERNAME", "value": username}, 
                {"key": "PASSWORD", "value": password},
                {"key": "STORAGE_CLASS", "value": storage_class},           
                {"key": "SIZE", "value": size},           
             ]
            }
            print("form data",formData)
            response = trigger_single(base_url, project_id_gitlab, headers, user_id, formData)
            print("OpenShift Standalone branch trigger.....")
            if response == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,   
                    backup_method="StorageClass/"+storage_class,
                    provider=provider_name,
                    
                )
                cluster.save()
                # Get and save artifacts
                pipeline_id = pipeline_dict.get(user_id)[0]
                print("pipeline_id ni :", pipeline_id)
                artifacts = get_latest_pipeline_artifacts(base_url, project_id_gitlab, headers, pipeline_id, cluster_name, cluster_type, database_version, provider_name, user_id,  project)
                print("New Artifacts:", artifacts)  # Print the artifacts
                cluster.artifacts = artifacts
                serializer = ClusterSerializers(cluster)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:  
                # Cluster creation failed
                Cluster_History.objects.create(
                    userID=user,
                    clustername=cluster_name,
                    cluster_status='failed'
                )           
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        elif provider_name == 'OpenShift' and cluster_type == 'Multiple':
            formData = {
                "ref": 'openshift-ha',
                "variables": [
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "OPN_USERNAME", "value": OpenShift_username},
                {"key": "OPN_PASSWORD", "value": OpenShift_password},
                {"key": "API_URL", "value": api_url},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "USERNAME", "value": username}, 
                {"key": "PASSWORD", "value": password},
                {"key": "STORAGE_CLASS", "value": storage_class},           
                {"key": "SIZE", "value": size},           
             ]
            }
            response = trigger_single(base_url, project_id_gitlab, headers, user_id, formData)
            print("OpenShift HA branch trigger.....")
            if response == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method="StorageClass/"+storage_class,
                    provider=provider_name,
                    
                )
                cluster.save()
                # Get and save artifacts
                pipeline_id = pipeline_dict.get(user_id)[0]
                print("pipeline_id ni :", pipeline_id)
                artifacts = get_latest_pipeline_artifacts(base_url, project_id_gitlab, headers, pipeline_id, cluster_name, cluster_type, database_version, provider_name, user_id,  project)
                print("New Artifacts:", artifacts)  # Print the artifacts
                cluster.artifacts = artifacts

                serializer = ClusterSerializers(cluster)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:  
                # Cluster creation failed
                Cluster_History.objects.create(
                    userID=user,
                    clustername=cluster_name,
                    cluster_status='failed'
                )           
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        
            
               
    @action(detail=False, methods=['get'])
    def check_cluster_exists(self, request, *args, **kwargs):
 
        cluster_name = request.query_params.get('cluster_name', None)
        project_id = request.query_params.get('project_id', None)
 
        if not cluster_name or not project_id:
            return Response({"error": "Cluster name and project ID are required parameters."}, status=status.HTTP_400_BAD_REQUEST)
 
        existing_cluster = Cluster.objects.filter( cluster_name=cluster_name,project_id=project_id).exists()
 
        if existing_cluster:
            return Response({"exists": True}, status=status.HTTP_200_OK)
        else:
            return Response({"exists": False}, status=status.HTTP_200_OK)
   
    
    def get_pipeline_status(self, request):
        global pipeline_dict
        user_id =  request.user.id
        # pipeline_id = pipeline_dict.get(user_id)[0]
        pipeline_id = pipeline_dict.get(user_id)[-1] if user_id in pipeline_dict and pipeline_dict[user_id] else None
        if (pipeline_id == None):
            return JsonResponse({"status": "No running cluster found"})
        else:
            # Replace these variables with your actual GitLab project ID and private token
            project_id = os.getenv('PROJECT_ID')
            private_token = os.getenv('PRIVATE_TOKEN')
            base_url = os.getenv('BASE_URL')
            headers = {"PRIVATE-TOKEN": private_token}
            # pipeline_count = 1
            artifacts = None
            pipeline_status = get_latest_pipeline_statuses(base_url, project_id, headers, pipeline_id)
            pipeline_logs = fetch_gitlab_pipeline_logs(private_token, base_url, project_id, pipeline_id)
            pipeline_logs.reverse()
            return JsonResponse({"status": pipeline_status,"artifacts": artifacts, "logs": pipeline_logs})
 
    def get_dele_pipeline_status(self,request):
        global pipeline_dict
        user_id =  request.user.id
        pipeline_id = pipeline_dict.get(user_id)[-1] if user_id in pipeline_dict and pipeline_dict[user_id] else None
        if (pipeline_id == None):
            return JsonResponse({"status": "No running cluster found"})
        else:
            # Replace these variables with your actual GitLab project ID and private token
            project_id = os.getenv('PROJECT_ID')
            private_token = os.getenv('PRIVATE_TOKEN')
            base_url = os.getenv('BASE_URL')
            headers = {"PRIVATE-TOKEN": private_token}
            pipeline_status = get_latest_pipeline_statuses(base_url, project_id, headers, pipeline_id)
            return JsonResponse({"status": pipeline_status})


# Define a logger for cluster-related actions
deletecluster_logger = logging.getLogger('deletecluster_logger')    

class ClusterDeleteViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        deleteCluster_name = request.data.get('cluster_name')
        provider_name = request.data.get('provider_name')
        user_id = request.user.id
        user_email = request.user.email  # Get the email of the logged-in user


        try:
            cluster = Cluster.objects.get(cluster_name=deleteCluster_name)
            storage_method = cluster.backup_method
            user_token = Token.objects.get(user=request.user).key
            is_pgadmin4 = cluster.is_pgadmin4  # Fetch the is_pgadmin4 value from the database
            print("is_pgadmin4 value : " , is_pgadmin4)
            
        except Cluster.DoesNotExist:
            return Response({"error": "Cluster not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            deletecluster_logger.error(f"Error retrieving cluster: {str(e)}")
            return Response({"error": f"Error retrieving cluster: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            provider = Provider.objects.filter(provider_name=provider_name, user_id=user_id).first()
            if not provider:
                return Response({"error": "Provider not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            deletecluster_logger.error(f"Error retrieving provider: {str(e)}")
            return Response({"error": f"Error retrieving provider: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            log_entry = f"user={cluster.user.username} clusterName={cluster.cluster_name} msg={cluster.cluster_name} deleted"
            deletecluster_logger.info(log_entry)
            
            # Prepare data for pipeline trigger
            formData = self._prepare_pipeline_data(provider, deleteCluster_name, storage_method, user_token)
            response = trigger_single(os.getenv('BASE_URL'), os.getenv('PROJECT_ID'), {"PRIVATE-TOKEN": os.getenv('PRIVATE_TOKEN')}, user_id, formData)
            user = User.objects.get(pk=user_id)
            pipeline_id = response[1]
            if response[0] == 200:
                Cluster_History.objects.create(
                userID = user,
                clustername=deleteCluster_name,
                cluster_status='deleted'  
                )
 
                cluster.delete()
                db_delete = Db_credentials.objects.get(cluster_name=deleteCluster_name)
                db_delete.delete()
                
                if is_pgadmin4:  # Check if is_pgadmin4 is True
                    try:
                        # **Remove server from pgAdmin using the user's email and pg_db_name**
                        if deleteCluster_name:  # Ensure pg_db_name is not blank
                            remove_command = [
                                '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/bin/python3',
                                '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/lib/python3.8/site-packages/pgadmin4/setup.py',
                                'remove-server',
                                deleteCluster_name,  # Use the pg_db_name fetched earlier
                                '--user',
                                user_email  # Use the logged-in user's email
                            ]
                            # Execute the command to remove the server
                            subprocess.run(remove_command, check=True)
                            print(f"Successfully removed server: {deleteCluster_name} for user: {user_email}")
                        else:
                            print(f"For this cluster {deleteCluster_name}, skipping server removal.")
                    except subprocess.CalledProcessError as e:
                        deletecluster_logger.error(f"Error removing server from pgAdmin: {str(e)}")
                        return Response({"error": f"Error removing server from pgAdmin: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    print("Skipping pgAdmin server removal as is_pgadmin4 is set to False.")


                # Remove pipeline ID from the dictionary after successful server removal
                time.sleep(5)
                pipeline_dict[user_id].remove(pipeline_id)

                return Response({"message": "Destroy pipeline triggered successfully."}, status=status.HTTP_200_OK)
            else:
                time.sleep(5)
                pipeline_dict[user_id].remove(pipeline_id)
                return Response({"error": "Failed to trigger Destroy pipeline."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            deletecluster_logger.error(f"Error during cluster deletion process: {str(e)}")
            return Response({"error": f"Error during cluster deletion process: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _prepare_pipeline_data(self, provider, deleteCluster_name, storage_method, user_token):
        """
        Prepare the data to be sent to the pipeline trigger based on the provider details and cluster name.
        """
        bitblast_ip = "172.16.1.100"
        return {
            "ref": self._get_branch_name(provider.provider_name),
            "variables": [
                {"key": "DATABASE_NAME", "value": deleteCluster_name},
                {"key": "STORAGE_METHOD", "value": storage_method},
                {"key": "TOKEN", "value": user_token},
                {"key": "BITBLAST_IP", "value": bitblast_ip},
                {"key": "PROVIDER_ENDPOINT", "value": provider.provider_url},
                {"key": "PROVIDER_SECRET_KEY", "value": provider.secret_key},
                {"key": "PROVIDER_ACCESS_KEY", "value": provider.access_token},
                {"key": "KUBE_CONFIG", "value": provider.kubeconfig_data},
                {"key": "OPN_USERNAME", "value": provider.OpenShift_username},
                {"key": "OPN_PASSWORD", "value": provider.OpenShift_password},
                {"key": "API_URL", "value": provider.api_url}
            ]
        }

    def _get_branch_name(self, provider_name):
        """
        Get the branch name based on the provider name.
        """
        if provider_name == 'Kubernetes':
            return 'rke2-db-delete'
        elif provider_name == 'OpenShift':
            return 'remove-db'
        else:
            return 'cloudstack-delete'


class DeletedClusterListView(generics.ListAPIView):
    serializer_class = ClusterHistorySerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Cluster_History.objects.filter(userID=user, cluster_status='deleted')

class DeleteClusterView(generics.DestroyAPIView):
    serializer_class = ClusterHistorySerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        cluster_name = self.kwargs.get('name')
        user = request.user

        try:
            # Retrieve the cluster by name and user
            cluster = Cluster_History.objects.get(userID=user, name=cluster_name, cluster_status='deleted')
            cluster.delete()  # Delete the cluster
            return Response({"message": "Cluster deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Cluster_History.DoesNotExist:
            return Response({"error": "Cluster not found."}, status=status.HTTP_404_NOT_FOUND) 


class ClusterHistoryViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    def list(self, request):
        """Get all cluster histories for the authenticated user."""
        user = request.user
        cluster_histories = Cluster_History.objects.filter(userID=user)
        serializer = ClusterHistorySerializers(cluster_histories, many=True)
        return Response(serializer.data)

    def destroy(self, request, name=None):
        """Delete a specific cluster history by cluster name."""
        try:
            cluster_history = Cluster_History.objects.get(clustername=name, userID=request.user)
            cluster_history.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Cluster_History.DoesNotExist:
            return Response({"error": "Cluster not found"}, status=status.HTTP_404_NOT_FOUND)





pipeline_dict = {}

def trigger_single(base_url, project_id, headers, user_id, formData):
    global pipeline_dict
    response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=formData,
                             verify=False)
    print('response',response.status_code)
    if response.status_code != 201:
        return {"error": f"Failed to create cluster. Status code: {response.status_code}"}
    pipeline_id = response.json().get("id")
    print(pipeline_id)
    # Update pipeline_dict with user_id and pipeline_id
    if user_id in pipeline_dict:
        pipeline_dict[user_id].append(pipeline_id)
    else:
        pipeline_dict[user_id] = [pipeline_id]
    pipeline_status = "pending"
    while pipeline_status in ["pending", "running"]:
        time.sleep(1)
        pipeline_info_response = requests.get(base_url + f"projects/{project_id}/pipelines/{pipeline_id}",
                                              headers=headers, verify=False)
        pipeline_info = pipeline_info_response.json()
        pipeline_status = pipeline_info.get("status")
    if pipeline_status == "success":
        return [200 , pipeline_id]
    else:
        return ["failed", pipeline_id]



def get_key_from_value(pipeline_dict, value):
    for key, values in pipeline_dict.items():
        if value in values:
            return key
    return None    
 
 
def get_latest_pipeline_statuses(base_url, project_id, headers, pipeline_id):
    response = requests.get(base_url + f"projects/{project_id}/pipelines/{pipeline_id}", headers=headers, verify=False)
 
    if response.status_code != 200:
        raise ValueError(f"Error fetching pipeline status: {response.status_code}, {response.json()}")
 
    pipeline_data = response.json()
    status = pipeline_data.get('status')
 
    return status

def get_latest_pipeline_artifacts(base_url, project_id, headers, pipeline_id, clusterName,clusterType,databaseVersion,providerName,userId, project):
    
    user = User.objects.get(pk=userId)
    print("user print : ", user)
    response = requests.get(base_url + f"projects/{project_id}/pipelines/{pipeline_id}/jobs", headers=headers, verify=False)
    if response.status_code != 200:
        raise ValueError(f"Error fetching pipeline jobs: {response.status_code}, {response.json()}")
 
    jobs = response.json()
    artifacts = []
    for job in jobs:
        response = requests.get(base_url + f"projects/{project_id}/jobs/{job['id']}/artifacts", headers=headers, verify=False)
        if response.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_file:
                # Modify the following to fetch the required artifacts
                required_artifacts = ['info.txt']
                for artifact_name in required_artifacts:
                    if artifact_name in zip_file.namelist():
                        content = zip_file.read(artifact_name).decode('utf-8')
                        artifacts.append({"filename": artifact_name, "content": content})
                     
                        existing_artifact = Db_credentials.objects.filter(
                            pipeline_id=pipeline_id,
                            filename=artifact_name
                        ).first()
 
                        if existing_artifact:
                            # Update the content of the existing artifact
                            existing_artifact.content = content
                            existing_artifact.save()
                        else:
                            # Create a new Db_credentials instance and save it to the database
                            artifact = Db_credentials(
                                user = user,
                                project = project,
                                cluster_name = clusterName,
                                cluster_type = clusterType,
                                database_version= databaseVersion,
                                provider_name= providerName,
                                pipeline_id=pipeline_id,
                                filename=artifact_name,
                                content=content,
                            )
                            artifact.save()
 
    return artifacts
 

def fetch_gitlab_pipeline_logs(private_token, base_url, project_id, pipeline_id):
    def clean_logs(log):
        # Remove ANSI escape sequences
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', log)
    def filter_and_map_logs(log, job_name):
        lines = log.splitlines()
        filtered_logs = []
        seen_logs = set()  # To avoid duplicate log entries
        play_recap_found = False
        first_log_line = True  # Flag to capture the first log line
        for line in lines:
            mapped_log = None
            # Only apply this custom message if the job name is "validate"
            if first_log_line and "validate" in job_name.lower():
                mapped_log = "Resources are being gathered."
                first_log_line = False  # Reset after the first line
            # Map specific logs to custom frontend messages
            if "Success! The configuration is valid." in line:
                mapped_log = "Preparing your environment for setup."
            elif "Plan:" in line and "to add" in line:
                mapped_log = "Getting everything ready for your request."
            elif "Terraform will perform the following actions:" in line:
                mapped_log = "Starting the setup process. This may take a few moments."
            elif "module." in line and "provisioner" in line:
                mapped_log = "Setting up the required components."
            elif "Apply complete! Resources:" in line:
                mapped_log = "Almost done with the setup."
            elif "Destroy complete! Resources:" in line:
                mapped_log = "Resources cleanup completed."
            elif "An execution plan has been generated" in line:
                mapped_log = "Moving to the next step."
            elif "TASK [Gathering Facts]" in line:
                mapped_log = "Getting things ready for data configuration."
            elif "TASK [Configure PostgreSQL]" in line:
                mapped_log = "Finalizing the setup of your data."
            elif "TASK [Install packages]" in line:
                mapped_log = "Applying important settings."
            elif "TASK [Start services]" in line:
                mapped_log = "Ensuring everything is set up securely."
            elif "TASK [Configure firewall rules]" in line:
                mapped_log = "Configuring access settings."
            elif "Error: Error creating the new instance" in line:
                error_start = line.find('"errortext":"') + len('"errortext":"')
                error_end = line.find('"', error_start)
                if error_start != -1 and error_end != -1:
                    error_message = line[error_start:error_end].rstrip('{\\')
                    mapped_log = f"There was an error creating the instance: {error_message}"
            elif "PLAY RECAP" in line:
                play_recap_found = True
            elif play_recap_found and line.strip():
                if "failed=0" in line:
                    mapped_log = "Your setup is complete and ready to use. Testing to ensure everything works correctly."
                else:
                    mapped_log = "Testing to ensure everything works correctly. There were some failures during the setup."
                play_recap_found = False
            else:
                play_recap_found = False
            if mapped_log and mapped_log not in seen_logs:
                filtered_logs.append(mapped_log)
                seen_logs.add(mapped_log)
        return filtered_logs
    headers = {'PRIVATE-TOKEN': private_token}
    try:
        # Fetch jobs for the specified pipeline
        jobs_url = f'{base_url}/projects/{project_id}/pipelines/{pipeline_id}/jobs'
        jobs_response = requests.get(jobs_url, headers=headers)
        jobs_response.raise_for_status()
        jobs = jobs_response.json()
        all_logs = []
        for job in jobs:
            job_id = job['id']
            job_name = job['name']
            # Fetch job trace logs
            log_url = f'{base_url}/projects/{project_id}/jobs/{job_id}/trace'
            log_response = requests.get(log_url, headers=headers)
            log_response.raise_for_status()
            job_logs = log_response.text
            # Clean ANSI escape sequences
            cleaned_logs = clean_logs(job_logs)
            # Filter and map to relevant log lines and user-friendly messages
            relevant_logs = filter_and_map_logs(cleaned_logs, job_name)
            if relevant_logs:  # Only append if we have relevant logs
                all_logs.append({
                    'job_name': job_name,
                    'job_id': job_id,
                    'logs': relevant_logs  # Store only the filtered logs
                })
        return all_logs
    except requests.exceptions.RequestException as e:
        print(f"Error fetching pipeline logs: {e}")
        return []
 
 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def display_artifacts(request):
    # Retrieve all saved artifacts from the database
    artifacts = Db_credentials.objects.all()
 
    # Prepare a list to hold artifact data
    artifacts_data = []
 
    for artifact in artifacts:
        artifact_data = {
            'clusterName' : artifact.clusterName,
            'pipeline_id': artifact.pipeline_id,
            'filename': artifact.filename,
            'content': artifact.content,
            
        }
        artifacts_data.append(artifact_data)
 
    return JsonResponse({'artifacts': artifacts_data})
 

def extract_host(content):

    import re

    match = re.search(r'Host:\s*([\d\.]+)', content)

    if match:

        return match.group(1)

    return None

def extract_port(content):

    import re

    match = re.search(r'Metrics Port:\s*([\d\.]+)', content)

    if match:

        return match.group(1)

    return None

def extract_ip(content):
    match = re.search(r'-h\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', content)
    return match.group(1) if match else None

@api_view(['GET'])
def display_clusters(request):
 
    clusters = Db_credentials.objects.all()
 
    # Prepare a list to hold cluster data
    clusters_data = []
 
    for cluster in clusters:
        if cluster.provider_name == 'CloudStack':
            target = f"{extract_host(cluster.content)}:9187" , f"{extract_host(cluster.content)}:9100"
        elif cluster.provider_name == 'Kubernetes':
            target = f"{extract_ip(cluster.content)}:{extract_port(cluster.content)}"
        else:
            # Handle other cases if needed
            target = ""  # Default value
 
        cluster_data = {
            'targets': target,
            'labels': {
                'instance': cluster.cluster_name,
                'cluster_type': cluster.cluster_type,
                'database_version': cluster.database_version,
                'provider_name': cluster.provider_name,
                'user': cluster.user.username,
                'project': cluster.project.project_name,
            }
        }
        if cluster.cluster_type == 'Standalone':
            clusters_data.append(cluster_data)
 
    result_data = clusters_data
 
    return JsonResponse(result_data, safe=False)
 
 
def extract_endpoint(content, endpoint_type):
    # Regular expressions to extract different endpoints
    patterns = {
        'metrics': r'Metrics Endpoint:\s*"([^"]+)"',
        'health': r'Health Endpoint:\s*"([^"]+)"'
    }
    match = re.search(patterns.get(endpoint_type, ''), content)
    if match:
        return match.group(1)
    return None
 
def get_data(request):
    # Assuming you want to fetch for a specific cluster, you need to specify it
    cluster_name = request.GET.get("clusterName")
    print(cluster_name)
 
    # Fetch the artifact content from the database
    artifact = Db_credentials.objects.filter(
        cluster_name=cluster_name,
        filename='info.txt'
    ).first()
    
    if artifact is None:
        return JsonResponse({'error': 'No artifact found for the specified cluster'}, status=404)
    
    # Extract the API endpoint
    content = artifact.content
    api_endpoint = extract_endpoint(content, 'health')
    print(api_endpoint)
    
    if api_endpoint is None:
        return JsonResponse({'error': 'API endpoint not found in the artifact'}, status=404)
    
    # Fetch data from the extracted API endpoint
    response = requests.get(api_endpoint)
    
    if response.status_code != 200:
        return JsonResponse({'error': f'Error fetching data from {api_endpoint}'}, status=response.status_code)
    
    data = response.json()
    return JsonResponse(data)
 
 
 


from .serializers import ClusterSerializers
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_clusters_details(request):
    clusters = Cluster.objects.filter(user_id=request.user.id)
    serializer = ClusterSerializers(clusters, many=True)
    return Response(serializer.data)
 
 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_clusters_by_user(request):
    clusters = Cluster.objects.filter(user_id=request.user.id)
    serializer = ClusterSerializers(clusters, many=True)
    return Response(serializer.data)
 
 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_clusters_by_user_one(request):
    clusters = Cluster.objects.filter(user_id=request.user.id)
    paginator = CustomPagination()
    paginated_clusters = paginator.paginate_queryset(clusters, request)
    serializer = ClusterSerializers(paginated_clusters, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_clusters_by_project(request, project_id):
    clusters = Cluster.objects.filter(project_id=project_id)
    serializer = ClusterSerializers(clusters, many=True)
    return Response(serializer.data)
 

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_clusters_by_project_one(request, project_id):
    clusters = Cluster.objects.filter(project_id=project_id)
    paginator = CustomPagination()
    paginated_clusters = paginator.paginate_queryset(clusters, request)
    serializer = ClusterSerializers(paginated_clusters, many=True)
    return paginator.get_paginated_response(serializer.data)
 

from rest_framework import generics
from rest_framework.response import Response
from .models import Db_credentials
from .serializers import DbcredentialsSerializer
from django.shortcuts import get_object_or_404 

class ContentByClusterNameView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DbcredentialsSerializer

    def get_queryset(self):
        cluster_name = self.kwargs['cluster_name']
        # print("cluster_name", cluster_name)
        user_id = self.request.user.id
        # print("user_id", user_id)

        # Return all entries for the given cluster_name regardless of user_id
        return Db_credentials.objects.filter(cluster_name=cluster_name)

            
 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_backup_method_by_cluster_name(request, cluster_name):
    try:
        cluster = Cluster.objects.get(cluster_name=cluster_name)
        backup_method = cluster.backup_method
        return Response({'backup_method': backup_method}, status=status.HTTP_200_OK)
    except Cluster.DoesNotExist:
        return Response({'error': 'Cluster not found'}, status=status.HTTP_404_NOT_FOUND) 



def pg_dashboard(request,server_data):
    # Convert the dictionary to JSON format
    json_data = json.dumps(server_data, indent=4)
    # print("json_data :", json_data)
                
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
    user_email = request.user.email  # Fetching the user's email
    command = [
                '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/bin/python3',
                '/home/ubuntu/stable-code/bitblast-application/DBaas_project/myenv/lib/python3.8/site-packages/pgadmin4/setup.py',
                'load-servers',
                file_path,
                '--user',
                user_email
             ]

    # Execute the command
    try:
        subprocess.run(command, check=True)  # check=True will raise an error for non-zero exit codes
    except subprocess.CalledProcessError as e:
        return JsonResponse({"error": str(e)}, status=500)
                
    # Delay deletion of the JSON file by 5 seconds
    time.sleep(5)

    # Delete the JSON file after 5 seconds
    try:
        os.remove(file_path)  # Remove the file after the delay
        print(f"File {file_path} deleted successfully.")
    except OSError as e:
        print(f"Error: {file_path} : {e.strerror}")

