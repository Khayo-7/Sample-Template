# from incidents.models import *
from Template.forms import *
from Template.filters import *
from Template.serializers import *
# from incidents.forms import AlertUpdateForm

Common_Arguments =  {
                        'page_type' : "Form",
                        'action' : None,
                        'pdf_template' : None,
                        'form_template' : 'form.html',
                        'view_template' :'view.html',
                        'view_all_template' :'view_all.html',
                        'assurance_template' : 'assurance.html',
                        'main_template' :'myapp/main.html',
                        # 'success_url' : '/success/',
                        # 'update_form' : AlertUpdateForm,
                }

Search_Arguments =   { 
                        'app' : '',
                        'title' : 'Search',
                        'success_url' : '/myapp/search-results/',
                        'instance' : [],
                        'instance_type' :[],
                        'url_suffix' : 'search',
                        'view_all_url' :'view-all-searches',
                        'form' : SearchForm,
                        'filter' : None,
                        'serializer' : SearchSerializer,
                        }