from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from django.conf.global_settings import DATETIME_INPUT_FORMATS

# ISO 8601 datetime format to accept html5 datetime input values
DATETIME_INPUT_FORMATS += ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M"]


from model.models import *
        
class modelForm(forms.ModelForm):

#     started_at_date = forms.DateTimeField() 
#     started_at_time = forms.DateTimeField() 
    class Meta:
        model = model
        exclude = ('created_by', 'updated_by', 'status')
        
# class modelUpdateForm(forms.ModelForm):
#     class Meta:
#         model = model
#         exclude = ('created_by', 'updated_by', 'status')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['model_name'].widget.attrs.update({
#     'class': 'form-control mb-2 account-form', 'placeholder': 'model_Name'
# })

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['started_at'].widget.attrs.update({
#     'class': 'timepicker',
# })
   
class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        exclude = ('created_by', 'updated_by', 'status')


    def __init__(self, *args, **kwargs): 
        super(modelForm, self).__init__(*args, **kwargs) 
        # self.fields['model].widget.attrs['hidden'] = True
        # self.fields['model].disabled = True
        # self.fields['model].widget.attrs['readonly'] = True        

# class model_rm(forms.ModelForm):
    
#     # created_at = forms.CharField(hidden=True, max_length=255)
#     # updated_at = forms.CharField(hidden=True, max_length=255)
#     class Meta:
#         model = model_#         # fields = '__all__' 
#         exclude = ('created_by', 'updated_by', 'status')
#     # def __init__(self, *args, **kwargs): 
#     #     super(model_rm, self).__init__(*args, **kwargs) 
#     #     self.fields['created_by'].widget.attrs['hidden'] = True
#     #     self.fields['created_by'].disabled = True
#         # self.fields[updated_by].widget.attrs['readonly'] = True
#         # # self.fields['created_at'].disabled = True
#         # self.fields['updated_by'].disabled = True
#         # # self.fields['created_at'].disabled = True

# class ThatForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         # first call parent's constructor
#         super(ThatForm, self).__init__(*args, **kwargs)
#         # there's a `fields` property now
#         self.fields['desired_field_name'].required = False

# class ThatForm(ModelForm):
#   class Meta:
#     requireds = 
#     {
#        'text':False,
#     }


# class BillingForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super(BillingForm, self).__init__(*args, **kwargs)
#        self.fields['account'].queryset = Account.objects.all()
#        self.fields['refrence'].queryset = Billing.objects.all()

#     class Meta:
#         model   = Billing
#         fields  = ('account', 'refrence',  'amount', 'remarks', )













# class AddmodelForm(ModelForm):
#     class Meta:
#         model = model
#         fields = '__all__'

#         # fields = ('name', 'title', 'birth_date')
#         # labels = {
#         #     'model_name': _('model Writer'),
#         # }
#         # help_texts = {
#         #     'model_name': _('Some useful help text.'),
#         # }
#         # error_messages = {
#         #     'model_name': {
#         #         'max_length': _("This writer's name is too long."),
#         #     },
#         # }
#         # percentile = CharField(validators=[validate_percentile])
#         # field_classes = {
#         #     'model_name': IntegerField,
#         # }
#         # error_messages = {
#         #     NON_FIELD_ERRORS: {
#         #         'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
#         #     }
#         # }
#         #  widgets = {
#         #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
#         # }
# class UploadImageForm(ModelForm):
#     class Meta:
#         model = attachment
#         fields = ['image']

# class Enhanced(UploadImageForm):
#     def clean(self):
#         pass
#     # percentile = CharField(validators=[validate_percentile])
       
# class Restricted(Enhanced):
#     class Meta(UploadImageForm):
#         exclude = ('image',)
      
# # class EntryForm(forms.ModelForm):

# #     class Meta:
# #         model = model_# #         fields = '__all__' 

# # class UploadFileForm(forms.Form):
# #     title = forms.CharField(max_length=50)
# #     file = forms.FileField()
# # # multiple files
# #     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))