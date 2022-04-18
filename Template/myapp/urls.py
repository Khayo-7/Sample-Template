from django.urls import path

from myapp import views 
from myapp.views import *

app_name = 'myapp'

report = Report()

urlpatterns = [

    path("", views.index, name="index"), #mapping the homepage function

    # path("preview-pdf/<int:id>/<str:preference>/<str:state>/", myapp.preview_pdf, name="preview-pdf"), #mapping the homepage function
    # # path("preview-pdf/<int:id>/", myapp.LabelsView.as_view(), name="preview-pdf"), #mapping the homepage function
    # path("download-pdf/<int:id>/<str:preference>/<str:state>/", myapp.download_pdf, name="download-pdf"), #mapping the homepage function
    path("generate-pdf/<int:id>/<str:preference>/<str:state>/", myapp.generator_2, name="generate-pdf"), #mapping the homepage function
    # path("generate-report/", myapp.generate_report, name="generate-report"), #mapping the homepage function
                   
    
    path("view-all-reports/", report.view_all, name="view-all-reports"),
    path("add-report/", report.add, name="add-report"),
    path("view-report/<int:id>/", report.view, name="view-report"),
    path("update-report/<int:id>/", report.update, name="update-report"),
    path("delete-report/<int:id>/", report.delete, name="delete-report"),
    path("approve-report/<int:id>/", report.approve, name="approve-report"),
    path("reject-report/<int:id>/", report.reject, name="reject-report"),
    path("search-report/", report.search, name="search-report"),

    path("report/", report.index, name="report"),
    
   

]
