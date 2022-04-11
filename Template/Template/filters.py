from django_filters import DateFilter, CharFilter
import django_filters as filters
from django.db import models


class SearchFilter(filters.FilterSet):
    
    class Meta:
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
                        'widget': forms.CheckboxInput,
                    },
                },
            }
