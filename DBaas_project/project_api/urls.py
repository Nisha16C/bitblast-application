from django.contrib import admin
from django.urls import path, include
from project_api.views import *
 
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register(r'cluster', ClusterViewSet, basename="cluster")
router.register(r'clusters', ClusterViewSet2, basename="clusters")

router.register(r'delete-cluster', ClusterDeleteViewSet, basename="cluster1")
router.register(r'project', ProjectViewSet, basename='project')
router.register(r'projects', ProjectViewSet2, basename='projects')

 
urlpatterns = [
    
    path('project/user/', get_projects_by_user, name='get_projects_by_user'),
    path('projects/userlist/', get_projects_by_user_one, name='get_projects_by_user_one'),
    path('projects/username', get_projects_by_username, name='get_projects_by_username'),

 

    path("cluster/user/", get_clusters_by_user, name='get_clusters_by_user'),
    path("clusters/userlist/", get_clusters_by_user_one, name='get_clusters_by_user_one'),

    path("cluster/project/<int:project_id>/", get_clusters_by_project, name='get_clusters_by_project'),
    path("clusters/project-list/<int:project_id>/", get_clusters_by_project_one, name='get_clusters_by_project_one'),
    path('display_clusters/', display_clusters, name='display_clusters'),  
    path('get_pipeline_status/', ClusterViewSet.as_view({'post': 'get_pipeline_status'}), name='get-pipeline-status'),
    path('get_dele_pipeline_status/', ClusterViewSet.as_view({'post': 'get_dele_pipeline_status'}), name='get-del-pipeline-status'),
    path('display_artifacts/', display_artifacts, name='display_artifacts'),
    path('get_backup_method/<str:cluster_name>/', get_backup_method_by_cluster_name, name='get_backup_method_by_cluster_name'),
    path('result/content/<str:cluster_name>/', ContentByClusterNameView.as_view(), name='content-by-cluster-name'), 
    path('cluster/check_cluster_exists/', ClusterViewSet.as_view({'get': 'check_cluster_exists'}), name='check-cluster-exists'),
    path("project/<int:pk>/rename/", ProjectViewSet.as_view({'put': 'rename_project'}), name='rename-project'),
    path('compute_offerings/', ComputeOfferingsAPIView.as_view(), name='compute-offerings'), 
    path('flavors/', FlavorList.as_view(), name='flavor-list'),
    path("", include(router.urls)),
    path('list_storage_classes/', list_storage_classes, name='list_storage_classes'),
    path('K8s_storage_classes/', K8s_storage_classes, name='K8s_storage_classes' ),
    path('get-data/', get_data, name='get_data' ),
    path('db-delete-history/', DeletedClusterListView.as_view(), name='deleted-cluster-list'),
    path('cluster-history/', ClusterHistoryViewSet.as_view({'get': 'list'}), name='cluster-history-list'),
    path('cluster-history/<str:name>/', ClusterHistoryViewSet.as_view({'delete': 'destroy'}), name='cluster-history-delete'),


]
 