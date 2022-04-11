from myapp.models import *
from myapp.forms import *
from myapp.filters import *
from myapp.serializers import *
                
Common_Myapp_Arguments =  {
                        'app' : 'myapp',
#                         'page_type' : "Form",
#                         'action' : None,
#                         'template' : 'form.html',
#                         'view_template' :'view.html',
#                         'view_all_template' :'view_all.html',
#                         'delete_template' : 'delete.html',
#                         # 'success_url' : '/success/',
                }

Report_Arguments =   { 
                        'title' : 'Reports',
                        'success_url' : '/myapp/view-all-reports',
                        'instance' : Report,
                        'instance_type' :'Report',
                        'url_suffix' : 'report',
                        'view_all_url' :'view-all-reports',
                        'main_template' :'myapp/report.html',
                        'form' : ReportForm,
                        'filter' : ReportFilter,
                        'serializer' : ReportSerializer,
                        }