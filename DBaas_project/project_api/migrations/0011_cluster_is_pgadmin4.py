# Generated by Django 3.2.25 on 2024-11-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_api', '0010_remove_cluster_pg_db_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='is_pgadmin4',
            field=models.BooleanField(default=False),
        ),
    ]
