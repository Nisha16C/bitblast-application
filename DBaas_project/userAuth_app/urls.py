from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userAuth_app.views import *
from .views import *

router = DefaultRouter()
router.register(r'login', LoginViewSet, basename='login')
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),

    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('d-login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('ldap-login/', LDAPLoginView.as_view(), name='lda-user-login'),
    path('role/', UserRoleView.as_view(), name='user-role'),
    path('save-ad-groups/', get_ADgroup_users, name='get_ADgroup_users'),    
    path('list-gmember/', list_ad_groups_with_members, name='list_ad_groups_with_members'),
    path('users/', UserListView.as_view(), name='user-list'),  # Add this line
    path('is-connected/', IsConnectedAPIView.as_view(), name='user-list'),  # Add this line
    path('save-ad-users/', save_ad_users, name='save_ad_users'),
    path('users/<str:username>/assign-role/', assign_or_change_role, name='assign_or_change_role'),
    path('users/<str:username>/user-role/', UserRoleAPIView.as_view(), name='user_role_api'),
    path('assign-role-group/', assign_roles_to_adgroup_members, name='assign_roles_to_adgroup_members'),
    path('fetch-group-role/<str:group_name>/', get_adgroup_role, name='get_adgroup_role'),
    path('get-user-info/', user_details, name='user_details'),   
    path('create_first_admin/', CreateFirstAdminAPIView.as_view(), name='create_first_admin'),
    path('check-admin-user-exists/', check_admin_user_exists, name='check_admin_user_exists'),
    path('users/<str:username>/toggle-status/', UserViewSet.as_view({'patch': 'toggle_user_status'}), name='toggle-user-status'),
    path('users/status/<str:username>/', UserViewSet.as_view({'patch': 'toggle_user_status'}), name='toggle-user-status'),
    path('reset-password/<str:username>/', ResetPasswordView.as_view(), name='reset-password'),



    # Other paths...
    

]