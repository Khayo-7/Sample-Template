import base64
import datetime
from io import BytesIO
from django import template
from Incident_Reporting.trans import *
import urllib

register = template.Library()

# @register.filter(name="get_encoded_dict")
# def get_encoded_dict(data_dict):
#     if data_dict is not None:
#         return urllib.parse.urlencode(data_dict)
#     return data_dict

@register.simple_tag(name='to_view_name')
def to_view_name(app, action, suffix):
    
    return str(app) + ':' + str(action) + '-' + str(suffix)

@register.simple_tag(name='now')
def now():
    now = datetime.datetime.utcnow().strftime('%H:%M:%S %d-%m-%Y') 
    return str(datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y') )

@register.filter(name='bin_2_img')
def bin_2_img(bin_data):
    
    if bin_data is not None and isinstance(bin_data, memoryview):
            return  'data:image/png;base64,' + base64.b64encode(bin_data).decode('utf-8')
    else:
        return bin_data


@register.filter(name='field_name_to_phrase')
def field_name_to_phrase(field_name):
    if field_name is not None: 
        try: 
            return  phrases[field_name]
        except:    
            return  field_name
        
@register.filter(name='get_all_field_value_pairs')        
def get_all_field_value_pairs(instance):
    if instance is not None: 
        # return [field.name for field in instance._meta.fields]
        if instance._meta.fields:
            return [(field.name, field.value_to_string(instance)) for field in instance._meta.fields]
        else:
            return []

@register.filter(name='return_first_instance')        
def return_first_instance(instances):
    if instances is not None: 
        return instances[0]
       

@register.filter(name='get_field_names_from_instance')        
def get_field_names_from_instance(instance):
    if instance is not None: 
        if instance._meta.fields:
            return [field.name for field in instance._meta.fields]
        else:
            return []

@register.filter(name='get_field_names_from_instances')        
def get_field_names_from_instances(instances):
    if instances is not None: 
        instance = instances.values()[0]
        if instance:
            return [field_name for field_name in instance.keys()]
        else:
            return []

