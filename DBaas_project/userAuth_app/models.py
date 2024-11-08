# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Standard', 'Standard'),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)  # Add this line to manage user activity


class LDAPGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
 
    def __str__(self):
        return self.name
 
class LDAPGroupMember(models.Model):
    group = models.ForeignKey(LDAPGroup, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
 
    class Meta:
        unique_together = ('group', 'username')
 
    def __str__(self):
        return f"{self.group} - {self.username}"
 
 
class ADGroupRoleAssignment(models.Model):
    group_name = models.CharField(max_length=100, unique=True)
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.group_name} - {self.role_name}"       
     
      