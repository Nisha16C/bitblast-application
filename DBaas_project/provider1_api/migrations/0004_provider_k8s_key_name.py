# Generated by Django 4.2.13 on 2024-08-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider1_api', '0003_add_new_providers'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='K8s_key_name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
