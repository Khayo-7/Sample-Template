from django.http import Http404
from django.contrib import messages
from django.forms.models import model_to_dict
from django.db import IntegrityError, transaction
from django.shortcuts import render, redirect, reverse, get_object_or_404
# Create your views here.
from Template.trans import *
from Template.arguments import *
from Template.general import General

from myapp.arguments import *
from myapp.serializers import *
from myapp.models import *

def index(request):
    title = "Index"
    page_type = "Page"
    template_name = 'myapp/index.html'  
    
    return render(request, template_name, context={'title': title, 'page_type':page_type})
   
def homepage(request):

    myapp = myapp.objects.all()
    total_myapp = myapp.count()
    context = {
        'myapp': myapp,  
        'total_myapp': total_myapp,
    }

class Report(General):

    def __init__(self):      
        super().__init__({**Common_Arguments,**Common_myapp_Arguments, **Report_Arguments})

def myapp_reports(request, instances):
    pass
