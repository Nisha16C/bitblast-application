from django.contrib import admin
from .models import Provider, MainProvider

# Register your models here.
admin.site.register (Provider)
admin.site.register (MainProvider)