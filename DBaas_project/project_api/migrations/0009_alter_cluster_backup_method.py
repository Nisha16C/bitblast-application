# Generated by Django 3.2.25 on 2024-10-15 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_api', '0008_cluster_pg_db_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='backup_method',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
