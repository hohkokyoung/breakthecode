from rest_framework import permissions

class IsInGroup(permissions.BasePermission):
    def __init__(self, group_name):
        self.group_name = group_name

    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name=self.group_name).exists()