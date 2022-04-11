from django.db import models
from django_filters import DateFilter, CharFilter
import django_filters as filters

from users.models import *
        
class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = '__all__'
        filter_overrides = {
             models.CharField: {
                 'filter_class': filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
             models.BooleanField: {
                 'filter_class': filters.BooleanFilter,
                 'extra': lambda f: {
                     'widget': forms.CheckboxInput,
                 },
             },
         }

class GroupFilter(filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr='icontains')
    start_date = DateFilter(field_name="created_at", lookup_expr='gte')
    end_date= DateFilter(field_name="created_at", lookup_expr='lte')
    class Meta:
        model = Group
        fields = '__all__'
        filter_overrides = {
             models.CharField: {
                 'filter_class': filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
             models.BooleanField: {
                 'filter_class': filters.BooleanFilter,
                 'extra': lambda f: {
                     'widget': forms.CheckboxInput,
                 },
             },
         }

class ContentFilter(filters.FilterSet):
    
    class Meta:
        model = Content
        fields = '__all__'
        filter_overrides = {
             models.CharField: {
                 'filter_class': filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
             models.BooleanField: {
                 'filter_class': filters.BooleanFilter,
                 'extra': lambda f: {
                     'widget': forms.CheckboxInput,
                 },
             },
         }

class PermissionFilter(filters.FilterSet):
    
    class Meta:
        model = Permission
        fields = '__all__'
        filter_overrides = {
             models.CharField: {
                 'filter_class': filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
             models.BooleanField: {
                 'filter_class': filters.BooleanFilter,
                 'extra': lambda f: {
                     'widget': forms.CheckboxInput,
                 },
             },
         }

class LevelFilter(filters.FilterSet):
    
    class Meta:
        model = Level
        fields = '__all__'
        filter_overrides = {
             models.CharField: {
                 'filter_class': filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
        }

class RoleFilter(filters.FilterSet):
    
    class Meta:
        model = Role
        fields = '__all__'
        filter_overrides = {
             models.CharField: {
                 'filter_class': filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
        }

# class UserGroupFilter(filters.FilterSet):
#     class Meta:
#         model = UserGroup
#         fields = '__all__'
#         exclude = ['attached_image', 'attached_image_data']
#         filter_overrides = {
#              models.CharField: {
#                  'filter_class': filters.CharFilter,
#                  'extra': lambda f: {
#                      'lookup_expr': 'icontains',
#                  },
#              },
#              models.BooleanField: {
#                  'filter_class': filters.BooleanFilter,
#                  'extra': lambda f: {
#                      'widget': forms.CheckboxInput,
#                  },
#              },
#          }

# class UserRoleFilter(filters.FilterSet):
#     class Meta:
#         model = UserRole
#         fields = '__all__'
#         filter_overrides = {
#              models.CharField: {
#                  'filter_class': filters.CharFilter,
#                  'extra': lambda f: {
#                      'lookup_expr': 'icontains',
#                  },
#              },
#              models.BooleanField: {
#                  'filter_class': filters.BooleanFilter,
#                  'extra': lambda f: {
#                      'widget': forms.CheckboxInput,
#                  },
#              },
#          }

# class GroupRoleFilter(filters.FilterSet):
#     class Meta:
#         model = GroupRole
#         fields = '__all__'
#         filter_overrides = {
#              models.CharField: {
#                  'filter_class': filters.CharFilter,
#                  'extra': lambda f: {
#                      'lookup_expr': 'icontains',
#                  },
#              },
#              models.BooleanField: {
#                  'filter_class': filters.BooleanFilter,
#                  'extra': lambda f: {
#                      'widget': forms.CheckboxInput,
#                  },
#              },
#          }