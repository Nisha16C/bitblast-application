from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Provider
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from userAuth_app.models import User
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import MainProvider
from .serializers import MainProviderSerializer
from userAuth_app.permissions import IsAllowedRole


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        
        username = request.user  # Get the authenticated user
        provider_name = request.data.get('provider_name')
        Key_name = request.data.get('key_name')
        provider_url = request.data.get('provider_url')
        secret_key = request.data.get('secret_key')
        access_token = request.data.get('access_token')
        kubeconfig_data = request.data.get('kubeconfig_data')
        openStackusername = request.data.get('OpenstackUsername')
        tenant_name = request.data.get('tenant_name')
        openstackpassword = request.data.get('OpenstackPassword')
        auth_url = request.data.get('auth_url')
        region = request.data.get('region')
        OpenShift_username = request.data.get ('OpenShift_username')
        OpenShift_password = request.data.get ('OpenShift_password')
        api_url = request.data.get ('api_url')

        user=User.objects.get(username=username)
        print("user info", user.username)
        # Check if the provider with the same name exists for this user
        existing_provider = Provider.objects.filter(provider_name=provider_name, user_id=user.id).first()

        if existing_provider:
            # Update the existing provider
            existing_provider.provider_name = provider_name
            existing_provider.Key_name = Key_name
            existing_provider.secret_key = secret_key
            existing_provider.access_token = access_token
            existing_provider.kubeconfig_data = kubeconfig_data
            existing_provider.openStackuser = openStackusername
            existing_provider.tenant_name = tenant_name
            existing_provider.openstackpassword = openstackpassword
            existing_provider.auth_url = auth_url
            existing_provider.region = region
            existing_provider.OpenShift_username = OpenShift_username
            existing_provider.OpenShift_password = OpenShift_password
            existing_provider.api_url = api_url
            existing_provider.is_connected = True  # Assuming connection is successful
            existing_provider.save()

            serializer = ProviderSerializer(existing_provider)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Create a new provider
            provider = Provider(
                user_id=user.id,
                provider_name=provider_name,
                Key_name=Key_name,
                provider_url=provider_url,
                secret_key=secret_key,
                access_token=access_token,
                kubeconfig_data=kubeconfig_data,
                openStackuser=openStackusername,
                tenant_name=tenant_name,
                openstackpassword=openstackpassword,
                auth_url=auth_url,
                region=region,
                OpenShift_username=OpenShift_username,
                OpenShift_password=OpenShift_password,
                api_url=api_url,
                is_connected=True
            )
            provider.save()

            serializer = ProviderSerializer(provider)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_provider_by_name(self, request, provider_name):
        provider = get_object_or_404(Provider, provider_name=provider_name, user_id=request.user.id)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='user-providers')
    def get_provider_by_user_id(self, request):
        providers = Provider.objects.filter(user_id=request.user.id, is_connected=True)
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)
        

    def get_provider_by_username_and_name(self, request, provider_name):
        user = request.user
        providers = Provider.objects.filter(user_id=user.id, provider_name=provider_name)

        if not providers.exists():
            # Return 404 if no objects are found
            return Response({'detail': 'Provider not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize all matching providers
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


 
class ProviderListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        providers = MainProvider.objects.all()
        serializer = MainProviderSerializer(providers, many=True)
        return Response(serializer.data)

 
class ToggleProviderStatus(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAllowedRole]
    def post(self, request, provider_id):
        print(provider_id)
        provider = get_object_or_404(MainProvider, id=provider_id)
        provider.is_enabled = not provider.is_enabled
        provider.save()
        return Response({
            'provider_id': provider.id,
            'is_enabled': provider.is_enabled,
            'provider_name': provider.provider_name
        }, status=status.HTTP_200_OK)
    


class ProviderSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializerK8S
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter the providers by the authenticated user
        return Provider.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        username = request.user.username  # Get the authenticated user's username
        provider_name = request.data.get('provider_name')
        K8s_key_name = request.data.get('K8s_key_name')
        kubeconfig_data = request.data.get('kubeconfig_data')

        user = get_object_or_404(User, username=username)

        # Check if a provider with the same K8s_key_name exists for this user
        existing_provider = Provider.objects.filter(user=user, K8s_key_name=K8s_key_name).first()

        if existing_provider:
            # Update the existing provider's kubeconfig_data
            existing_provider.kubeconfig_data = kubeconfig_data
            existing_provider.is_connected = True  # Assuming connection is successful
            existing_provider.save()

            serializer = ProviderSerializerK8S(existing_provider)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Create a new provider with the provided fields
            provider = Provider(
                user_id=user.id,
                provider_name=provider_name,
                K8s_key_name=K8s_key_name,
                kubeconfig_data=kubeconfig_data,
                is_connected=True  # Assuming connection is successful
            )
            provider.save()

            serializer = ProviderSerializerK8S(provider)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



    @action(detail=False, methods=['get'], url_path='(?P<K8s_key_name>[^/.]+)')
    def retrieve_kubeconfig(self, request, K8s_key_name=None):
        provider = get_object_or_404(Provider, K8s_key_name=K8s_key_name)
        return Response({'kubeconfig_data': provider.kubeconfig_data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='k8s-key-names')
    def list_connected_key_names(self, request, *args, **kwargs):
        # Filter by authenticated user and connected providers
        connected_providers = Provider.objects.filter(user=request.user, is_connected=True)
        serializer = ProviderSerializerK8S(connected_providers, many=True)
        key_names = [provider['K8s_key_name'] for provider in serializer.data if provider['K8s_key_name'] is not None]
        return Response(key_names, status=status.HTTP_200_OK)

    @action(detail=False, methods=['delete'], url_path='k8s-key-names/(?P<K8s_key_name>[^/.]+)')
    def delete_provider(self, request, K8s_key_name=None):
        provider = get_object_or_404(Provider, K8s_key_name=K8s_key_name)
        provider.delete()
        return Response({'message': 'Provider deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

