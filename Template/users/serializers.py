from rest_framework import serializers
from users.models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'    

class ContentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Content
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Permission
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Level
        fields = '__all__'        

class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields = '__all__'        

# class UserGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserGroup
#         fields = '__all__'

# class UserRoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserRole
#         fields = '__all__'

# class GroupRoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupRole
#         fields = '__all__'