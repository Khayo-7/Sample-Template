from Incident_Reporting.serializers import *
from users.models import *
from users.forms import *
from users.filters import *
from users.serializers import *

                
Common_User_Arguments =  {
                        'app' : 'users',
#                         'page_type' : 'Form',
#                         'action' : None,
#                         'template' : 'form.html',
#                         'view_template' :'view.html',
#                         'view_all_template' :'view_all.html',
#                         'delete_template' : 'delete.html',
#                         # 'success_url' : '/success/',
                }

User_Arguments =   { 
                        'title' : 'Users',
                        'success_url' : '/users/view-all-users',
                        'instance' : User,
                        'instance_type' :'User',
                        'url_suffix' : 'user',
                        'view_all_url' :'view-all-users',
                        'form' : UserForm,
                        'filter' : UserFilter,
                        'serializer' : UserSerializer,
                        }

Group_Arguments =   { 
                        'title' : 'Groups',
                        'success_url' : '/users/view-all-groups',
                        'instance' : Group,
                        'instance_type' :'Group',
                        'url_suffix' : 'group',
                        'view_all_url' :'view-all-groups',
                        'form' : GroupForm,
                        'filter' : GroupFilter,
                        'serializer' : GroupSerializer,
                        }

Content_Arguments =   { 
                        'title' : 'Content',
                        'success_url' : '/users/view-all-contents',
                        'instance' : Content,
                        'instance_type' :'Content',
                        'url_suffix' : 'content',
                        'view_all_url' : 'view-all-contents',
                        'form' : ContentForm,
                        'filter' : ContentFilter,
                        'serializer' : ContentSerializer,
                        }

Permission_Arguments =   { 
                        'title' : 'Permissions',
                        'success_url' : '/users/view-all-permissions',
                        'instance' : Permission,
                        'instance_type' :'Permission',
                        'url_suffix' : 'permission',
                        'view_all_url' :'view-all-permissions',
                        'form' : PermissionForm,
                        'filter' : PermissionFilter,
                        'serializer' : PermissionSerializer,
                        }

Role_Arguments =   { 
                        'title' : 'Roles',
                        'success_url' : '/users/view-all-roles',
                        'instance' : Role,
                        'instance_type' :'Role',
                        'url_suffix' : 'role',
                        'view_all_url' :'view-all-roles',
                        'form' : RoleForm,
                        'filter' : RoleFilter,
                        'serializer' : RoleSerializer,
                        }

Level_Arguments =   { 
                        'title' : 'Levels',
                        'success_url' : '/users/view-all-levels',
                        'instance' : Level,
                        'instance_type' :'Level',
                        'url_suffix' : 'level',
                        'view_all_url' :'view-all-levels',
                        'form' : LevelForm,
                        'filter' : LevelFilter,
                        'serializer' : LevelSerializer,
                        }

# User_Group_Arguments =   { 
#                         'title' : 'User-Groups',
#                         # 'success_url' : '/users/view-all-user-groups',
#                         'success_url' : '/success/',
#                         'instance' : UserGroup,
#                         'instance_type' :'User-Group',
#                         'url_suffix' : 'user-group',
#                         'view_all_url' :'view-all-user-groups',
#                         'form' : UserGroupForm,
#                         'filter' : UserGroupFilter,
#                         'serializer' : UserGroupSerializer,
#                         }

# User_Role_Arguments =   { 
#                         'title' : 'User Roles',
#                         'success_url' : '/users/view-all-user-roles',
#                         'instance' : UserRole,
#                         'instance_type' :'User Role',
#                         'url_suffix' : 'user-role',
#                         'view_all_url' :'view-all-user-roles',
#                         'form' : UserRoleForm,
#                         'filter' : UserRoleFilter,
#                         'serializer' : UserRoleSerializer,
#                         }

# Group_Role_Arguments =   { 
#                         'title' : 'Group Roles',
#                         'success_url' : '/users/view-all-group-roles',
#                         'instance' : GroupRole,
#                         'instance_type' :'Group Role',
#                         'url_suffix' : 'group-role',
#                         'view_all_url' :'view-all-group-roles',
#                         'form' : GroupRoleForm,
#                         'filter' : GroupRoleFilter,
#                         'serializer' : GroupRoleSerializer,
#                         }
