from django.db import models
from django_filters import DateFilter, CharFilter
import django_filters as filters

from myapp.models import *
      
class ReportFilter(filters.FilterSet):
    asset_name = CharFilter(field_name="asset_name", lookup_expr='icontains')
    start_date = DateFilter(field_name="created_at", lookup_expr='gte')
    end_date= DateFilter(field_name="created_at", lookup_expr='lte')
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['file_attachment', 'file_attachment_data']
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
                     'widget': filters.CheckboxInput,
                 },
             },
         }