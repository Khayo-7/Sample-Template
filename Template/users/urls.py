from django.urls import path, include
from users import views  #importing our view file 
# from .views import Add_user_form
from django.urls import path
from users import views 
from users.views import * 

app_name = 'users'

user = User()
group = Group()
content = Content()
permission = Permission()
level = Level()
role = Role()
# user_group = UserGroup()
# user_role = UserRole()
# group_role = GroupRole()
search = Search()

urlpatterns = [
    path(r"", views.index, name="index"), #mapping the homepage function

    path("search/", group.search, name="search"),
    path("login/", group.search, name="login"),
    path("logout/", group.search, name="logout"),
    path("register/", group.search, name="register"),
    path("password-change/", group.search, name="password-change"),
                   
    path("view-all-users/", user.view_all, name="view-all-users"),
    path("add-user/", user.add, name="add-user"),
    path("view-user/<int:key>", user.view, name="view-user"),
    path("update-user/<int:key>", user.update, name="update-user"),
    path("delete-user/<int:key>", user.delete, name="delete-user"),


   
    path("view-all-groups/", group.view_all, name="view-all-groups"),
    path("add-group/", group.add, name="add-group"),
    path("view-group/<int:key>", group.view, name="view-group"),
    path("update-group/<int:key>", group.update, name="update-group"),
    path("delete-group/<int:key>", group.delete, name="delete-group"),

                 
    path("view-all-contents/", content.view_all, name="view-all-contents"),
    path("add-content/", content.add, name="add-content"),
    path("view-content/<int:key>", content.view, name="view-content"),
    path("update-content/<int:key>", content.update, name="update-content"),
    path("delete-content/<int:key>", content.delete, name="delete-content"),
                                     
    path("view-all-permissions/", permission.view_all, name="view-all-permissions"),
    path("add-permission/", permission.add, name="add-permission"),
    path("view-permission/<int:key>", permission.view, name="view-permission"),
    path("update-permission/<int:key>", permission.update, name="update-permission"),
    path("delete-permission/<int:key>", permission.delete, name="delete-permission"),
    
    path("view-all-roles/", role.view_all, name="view-all-roles"),
    path("add-role/", role.add, name="add-role"),
    path("view-role/<int:key>", role.view, name="view-role"),
    path("update-role/<int:key>", role.update, name="update-role"),
    path("delete-role/<int:key>", role.delete, name="delete-role"),
    
    path("view-all-levels/", level.view_all, name="view-all-levels"),
    path("add-level/", level.add, name="add-level"),
    path("view-level/<int:key>", level.view, name="view-level"),
    path("update-level/<int:key>", level.update, name="update-level"),
    path("delete-level/<int:key>", level.delete, name="delete-level"),
         
    # path("view-all-user-groups/", user_group.view_all, name="view-all-user-groups"),
    # path("add-user-group/", user_group.add, name="add-user-group"),
    # path("view-user-group/<int:key>", user_group.view, name="view-user-group"),
    # path("update-user-group/<int:key>", user_group.update, name="update-user-group"),
    # path("delete-user-group/<int:key>", user_group.delete, name="delete-user-group"),
                 
    # path("view-all-user-permission/", user_role.view_all, name="view-all-user-permission"),
    # path("add-user-permission/", user_role.add, name="add-user-permission"),
    # path("view-user-permission/<int:key>", user_role.view, name="view-user-permission"),
    # path("update-user-permission/<int:key>", user_role.update, name="update-user-permission"),
    # path("delete-user-permission/<int:key>", user_role.delete, name="delete-user-permission"),
   
    # # path("approve-user-permission/<str:key>", views.approve_group, name="approve-group"),
                  
    # path("view-all-group-permission/", group_role.view_all, name="view-all-group-permission"),
    # path("add-group-permission/", group_role.add, name="add-group-permission"),
    # path("view-group-permission/<int:key>", group_role.view, name="view-group-permission"),
    # path("update-group-permission/<int:key>", group_role.update, name="update-group-permission"),
    # path("delete-group-permission/<int:key>", group_role.delete, name="delete-group-permission"),

]
