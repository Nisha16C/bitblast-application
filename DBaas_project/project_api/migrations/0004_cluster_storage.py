# Generated by Django 4.2.9 on 2024-08-31 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_api', '0003_cluster_k8s_key_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='storage',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]