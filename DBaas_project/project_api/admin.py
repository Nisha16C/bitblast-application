from django.contrib import admin
from .models import Project, Cluster,Db_credentials,Cluster_History

# Register your models here.



admin.site.register(Db_credentials)
admin.site.register(Cluster_History)

# Register your models here.
admin.site.register (Project)
admin.site.register (Cluster)