from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, GroupViewSet, UserGroupUpgradeView

# Create a router instance
router = DefaultRouter()

# Register the UserViewSet
router.register(r'users', UserViewSet, basename='user')
router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
    path('groups/upgrade', UserGroupUpgradeView.as_view(), name='user-group-upgrade'),
]