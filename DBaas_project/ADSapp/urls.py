from django.urls import path , include
# from .views import update_ldap_settings
from ADSapp.views import *
# from .views import ActiveUserListView
from rest_framework import routers
from .views import get_ad_users , kubectl_command

router = routers.DefaultRouter()
router.register(r'update_ldap_settings', FormViewSet, basename='update_ldap_settings')
router.register(r'reset_ldap_settings', FormViewSet, basename='reset_ldap_settings')
# router.register(r'ldap-settings', LDAPSettingsViewSet, basename='ldap-settings')
urlpatterns = [
     # Define a URL pattern for accessing the LDAP users
    path('ad-users/', get_ad_users, name='ad_users_api'),
    path("", include(router.urls)),
    path('kubectl-execute/', kubectl_command, name='kubectl_command'),
    path('create-server-config/', CreateServerConfigView.as_view(), name='create-server-config'),  # Use .as_view() here 
    path('remove-server-config/', RemoveServerConfigView.as_view(), name='remove-server-config'),  # Use .as_view() here 
    path('create-pgadmin-user/', CreatePgAdminUserView.as_view(), name='create_pgadmin_user'),
    path('update-user-status/', UpdatePgAdminUserStatusView.as_view(), name='update-pgadmin-user-status'),



]