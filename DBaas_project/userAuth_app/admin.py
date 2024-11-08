from django.contrib import admin
from .models import User,LDAPGroup,LDAPGroupMember,ADGroupRoleAssignment

admin.site.register(User)
admin.site.register(LDAPGroup)
admin.site.register(LDAPGroupMember)
admin.site.register(ADGroupRoleAssignment)

