from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.postgres.search import SearchVector
from django.views.generic import FormView

# Create your views here.
# from Template.decorators import unauthenticated_user
from Template.arguments import *
from Template.general import General
from users.arguments import *
from users.models import *


# # @unauthenticated_user
def index(request):
    title = "Index"
    page_type = "Page"
    template_name = 'users/index.html'  
    
    return render(request, template_name, context={'title': title, 'page_type': page_type})

# User
class User(General):
    def __init__(self):        
        super().__init__({**Common_Arguments, **Common_User_Arguments, **User_Arguments})
      
# Group
class Group(General):
    def __init__(self):        
        super().__init__({**Common_Arguments, **Common_User_Arguments, **Group_Arguments})
     
# Content
class Content(General):
    def __init__(self):        
        super().__init__({**Common_Arguments, **Common_User_Arguments, **Content_Arguments})
       
# Permission
class Permission(General):
    def __init__(self):        
        super().__init__({**Common_Arguments, **Common_User_Arguments, **Permission_Arguments})
      
# Level
class Level(General):
    def __init__(self):        
        super().__init__({**Common_Arguments, **Common_User_Arguments, **Level_Arguments})
       
# Role
class Role(General):
    def __init__(self):        
        super().__init__({**Common_Arguments, **Common_User_Arguments, **Role_Arguments})
       
# # User_Group
# class UserGroup(General):
#     def __init__(self):        
#         super().__init__({**Common_Arguments, **Common_User_Arguments, **User_Group_Arguments})
       
# # class User_Role
# class UserRole(General):
#     def __init__(self):        
#         super().__init__({**Common_Arguments, **Common_User_Arguments, **User_Role_Arguments})
       
# # Group__Role 
# class GroupRole(General):
#     def __init__(self):        
#         super().__init__({**Common_Arguments, **Common_User_Arguments, **Group_Role_Arguments})
       
# Search
class Search(General):
    def __init__(self):        
        super().__init__({**Common_Arguments, **Common_User_Arguments, **Search_Arguments})

# Approve
class Approve(General):
    def __init__(self):        
        super().__init__({**Common_Arguments, **Common_User_Arguments, **Search_Arguments})
  
  



def approve_user(request, key):

    obj = General({**User_arguments, **asset_arguments})
    return obj.approve_deny(request, key)
    
def upload_photo(request):

    upload_object = General({**User_arguments, **upload_arguments})
    return upload_object.upload(request)

