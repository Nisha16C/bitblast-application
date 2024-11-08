from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project, Cluster, Db_credentials , Cluster_History

class projectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class ClusterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = "__all__"        
        
class ClusterHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Cluster_History
        fields = "__all__"
 

class DbcredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Db_credentials
        fields = ['content']              