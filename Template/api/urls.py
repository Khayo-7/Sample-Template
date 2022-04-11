from django.urls import path, include

from . import views 
from .views import *


from Template.arguments import *
from myapp.arguments import *
from users.arguments import *

app_name = 'api'

# general = General()


urlpatterns = [

    path(r"", views.getRoutes, name="getRoutes"), #mapping the homepage function
    # path(r"", General.as_view(), name="getRoutes"), #mapping the homepage function
    path(r"search/", views.search, name="api-search"), 
    path(r"all/", views.view_all, name="all"),
    path(r"add/", views.add, name="add"),
    path(r"view/<int:key>", views.view, name="view"),
    path(r"update/<int:key>", views.update, name="update"),
    path(r"delete/<int:key>", views.delete, name="delete"),
                 



  
]

