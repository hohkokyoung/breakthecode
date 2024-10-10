# from django.contrib.auth.models import User, Group
# from rest_framework.exceptions import ValidationError

# def get_user(user_id):
#     try:
#         user = User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         raise ValidationError("User does not exist.")
    
#     return user

# def get_group(group_id):
#     try:
#         group = Group.objects.get(id=group_id)
#     except User.DoesNotExist:
#         raise ValidationError("Group does not exist.")
    
#     return group