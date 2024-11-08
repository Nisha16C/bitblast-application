from django.db import migrations

def add_default_providers(apps, schema_editor):
    MainProvider = apps.get_model('provider1_api', 'MainProvider')
    default_providers = [
        {'provider_name': 'OpenStack', 'img_name': 'Openstack.png', 'is_enabled': False},
        {'provider_name': 'CloudStack', 'img_name': 'cloudstack.png', 'is_enabled': False},
 
	    {'provider_name': 'Harvester', 'img_name': 'harvester.jpg ', 'is_enabled': False},
	    {'provider_name': 'Nutanix', 'img_name': 'nutanix.png', 'is_enabled': False},
	    {'provider_name': 'OpenShift', 'img_name': 'openshift.png', 'is_enabled': False},
 
	    {'provider_name': 'Kubernetes', 'img_name': 'k8s.png', 'is_enabled': False},
	    {'provider_name': 'VMware', 'img_name': 'Vmware.png', 'is_enabled': False},

    ]
    for provider_data in default_providers:
        MainProvider.objects.create(**provider_data)

class Migration(migrations.Migration):
    dependencies = [
        ('provider1_api', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_default_providers),
    ]


 
 