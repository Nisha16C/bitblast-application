# Generated by Django 5.0.7 on 2024-07-23 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cluster',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterField(
            model_name='cluster',
            name='backup_method',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
