from rest_framework import generics, viewsets, status
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer, GroupIdSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from .enums import GroupName

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()] 
        return [permission() for permission in self.permission_classes]

class UserGroupUpgradeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = GroupIdSerializer(data=request.data)
        # although serializer.is_valid(raise_exception=True) can be used, this is personally more readable
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        group = Group.objects.get(id=serializer.validated_data['id'])

        if (group.name == GroupName.ADMIN.value):
            return Response({"detail": "Not allowed to upgrade the user to this group."})

        if group not in user.groups.all():
            user.groups.add(group)

        return Response({"success": True}, status=status.HTTP_200_OK)