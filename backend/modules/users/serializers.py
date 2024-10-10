# users/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.exceptions import ValidationError

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']

class GroupIdSerializer(serializers.ModelSerializer):
    # needed because id is a read-only field
    # source: https://www.django-rest-framework.org/api-guide/serializers/#customizing-multiple-update
    id = serializers.IntegerField()

    class Meta:
        model = Group
        fields = ['id']

    def validate_id(self, value):
        """
        Validate that the ID exists in the database.
        """
        if not Group.objects.filter(id=value).exists():
            raise ValidationError(f"Group with ID {value} does not exist.")
        return value

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

