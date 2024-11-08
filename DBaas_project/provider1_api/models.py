from django.db import models
# from django.contrib.auth.models import User
from userAuth_app.models import User


from django_prometheus.models import ExportModelOperationsMixin

class Provider(ExportModelOperationsMixin('provider'),models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=100)
    Key_name = models.CharField(max_length=100)
    K8s_key_name = models.CharField(max_length=100,unique=True, blank=True, null=True)


    provider_url = models.URLField(blank=True, null=True)
    secret_key =  models.CharField(max_length=100,  blank=True, null=True)
    access_token = models.CharField(max_length=100, blank=True, null=True )
    is_connected = models.BooleanField(default=False)  # New field
    kubeconfig_data = models.TextField(blank=True, null=True)

    # New fields for OpenStack provider
    openStackuser = models.CharField(max_length=100, null=True)
    tenant_name = models.CharField(max_length=100, null=True)
    openstackpassword = models.CharField(max_length=100, null=True)
    auth_url = models.URLField(null=True)
    region = models.CharField(max_length=100, null=True)
    OpenShift_username = models.CharField(max_length=100, null=True)
    OpenShift_password = models.CharField(max_length=100, null=True)
    api_url = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        if self.Key_name:
            return f'{self.provider_name} - {self.Key_name}'
        elif self.K8s_key_name:
            return f'{self.provider_name} - {self.K8s_key_name}'
        else:
            return self.provider_name
    

class MainProvider(models.Model):
    provider_name = models.CharField(max_length=255)
    img_name = models.CharField(max_length=255, blank=True, null=True)
    is_enabled = models.BooleanField(default=False)
 
    def __str__(self):
        return self.provider_name

