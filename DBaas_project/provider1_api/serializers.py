from userAuth_app.models import User
from userAuth_app.serializers import userAuthSerializers
from rest_framework import serializers
from .models import Provider, MainProvider

class ProviderSerializer(serializers.ModelSerializer):
    # user = userAuthSerializers()
    class Meta:
        model = Provider
        fields = "__all__"

class MainProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProvider
        fields = ['id', 'provider_name', 'img_name', 'is_enabled']

        
class ProviderSerializerK8S(serializers.ModelSerializer):
    # user = userAuthSerializers()
    class Meta:
        model = Provider
        fields = ['id', 'provider_name', 'K8s_key_name', 'kubeconfig_data']
 
