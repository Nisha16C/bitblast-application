
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from provider1_api.views import *

router = DefaultRouter()
router.register(r'providers', ProviderViewSet, basename='provider')
router.register(r'provider', ProviderSet, basename='provider1')


urlpatterns = [
    path('', include(router.urls)),
    # path('api/v1/providers/user/<int:user_id>/', get_provider_by_user_id, name='get-provider-by-user-id'),

    re_path(r'^providers/by-name/(?P<provider_name>[-\w]+)/$', 
            ProviderViewSet.as_view({'get': 'get_provider_by_name'}), 
            name='get-provider-by-name'),
    # re_path(r'^providers/by-user/', ProviderViewSet.as_view({'get': 'get_provider_by_user_id'}), name='get-provider-by-user-id'),

    path('providers/by-username-and-name/<str:provider_name>/', 
         ProviderViewSet.as_view({'get': 'get_provider_by_username_and_name'}), 
         name='get-provider-by-username-and-name'),
        path('toggle-provider-status/<int:provider_id>/', ToggleProviderStatus.as_view(), name='toggle_provider_status'),
        path('provider-list/', ProviderListView.as_view(), name='provider_list')
        ]

