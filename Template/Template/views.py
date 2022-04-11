from django.shortcuts import render
# Create your views here.

from Template.decorators import unauthenticated_user
from Template.general import General
from Template.arguments import *

#@unauthenticated_user
def index(request):
    return render(request, 'index.html', context={})
    
def home(request):
    return render(request, 'homepage.html', context={})

def about(request):
    return render(request, 'homepage.html', context={})

def contact(request):
    return render(request, 'homepage.html', context={})

def success(request):
    return render(request, 'success.html', context={})

def search(request):
    return render(request, 'form.html', context={})
         
# Search
class Search(General):
    def __init__(self):        
        super().__init__({**Common_Arguments, **Search_Arguments})
  
  