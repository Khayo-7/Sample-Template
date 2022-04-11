from django.utils.timezone import now
from django.db import models
from django.db.models import fields
from django.utils.translation import gettext_lazy as _

# Create your models here.
from users.models import User
from Template.validators import validate_percentage

PENDING = 'pending'
APPROVED = 'approved'
REJECTED = 'rejected'

STATUS_CHOICES = [
    (PENDING, _('Pending(Waiting for Processing)')),
    (APPROVED, _('Approved')),
    (REJECTED, _('Rejected')),
]
     
    class Meta:
        ordering = ['code']
        unique_together = (("code", "message"),)
        permissions = (
            ('approve_report', 'can approve reports'),
        )
    
    def __str__(self):
        return self.message + '(' + self.code + ')'

# class Attachment(models.Model):

#     image = models.ImageField(upload_to ='image_uploads/% Y/% m/% d/', null=True)
#     image_data = models.BinaryField(null=True) 

#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING, null=True) 

#     description = models.TextField(null=True, blank=True)    
#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='uploaded_file_created_by', null=True) 
#     created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
#     updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='uploaded_file_updated_by', null=True, blank=True) 
#     updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['ip']
        unique_together = (("id", "domain_name"),)

    def __str__(self):
        return self.domain_name + '(' + self.ip + ')'

#  type = forms.TypedChoiceField(choices=formfields.TYPE_CHOICES, initial='FIXED')
#     record = forms.TypedChoiceField(choices=formfields.RECORD_CHOICES, initial='FIXED')
#     hostname = forms.CharField(max_length=100)

#     def clean(self):  
#         cleaned_data = super(CacheCheck, self).clean()
#         record = cleaned_data.get("record")

#         if record == "PTR":
#             hostname = forms.GenericIPAddressField(label=("ip address"))
#         else record == "A":
#             hostname = forms.RegexField(label=("hostname"), max_length=31, regex=r'[a-zA-Z0-9-_]*\.[a-zA-Z]{2,6}'


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name 

    class Meta:
        ordering = ['name']
        unique_together = (("name", "address"),)

     
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING, null=True) 
    last_index = models.IntegerField(default=0)
    
    description = models.TextField(null=True, blank=True) 
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='asset_type_created_by', null=True) 
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='asset_type_updated_by', null=True, blank=True) 
    updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['code']
        unique_together = (("code", "name"),)
        # unique_together = (('name', 'game',), ('user', 'game',))
        # constraints = [
        #     models.UniqueConstraint(fields=['code', 'name'], name='code-name constraint')
        # ]
        # constraints = [
        #             UniqueConstraint(
        #                 Lower('code'),
        #                 Lower('name').desc(),
        #                 name='code_name_unique',
        #             ),
        #         ] 

    def __str__(self):
        return self.name + '(' + self.code + ')'

class myapp(models.Model):
 
    code = models.CharField(max_length=255,  unique=True)

    # started_at = models.DateTimeField(null=True)  # initial time
    # ended_at = models.DateTimeField(null=True)  # period  how many how long
    
    ip = models.GenericIPAddressField(protocol='IPv4', null=True)
   # 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING, null=True) 
    feedback = models.TextField(null=True, blank=True)
    
    description = models.TextField(null=True, blank=True)
    # analyst = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myapp_analyzed_by', null=True) 
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='myapp_created_by', null=True) 
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True) 
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='myapp_updated_by', null=True, blank=True)
    updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True, blank=True)

    # def get_fields(self):
    #     return [(field.name, field.value_to_string(self)) for field in myapp._meta.fields]

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.code 
    
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        print("here")
        return reverse('view-myapp', args=[self.id])
        # return "/myapp/view-myapp/%i/" % self.id

    myapp = models.ForeignKey(myapp, on_delete=models.SET_NULL, null=True)
    attachment_source = models.ForeignKey(AttachmentSource, on_delete=models.SET_NULL, related_name="attachment_source", null=True)
    
    attachment = models.ImageField(upload_to ='image_uploads/% Y/% m/% d/', null=True)
    attachment_data = models.BinaryField(null=True) 

class Report(models.Model):

    date = models.DateField(default=now)
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES, null=True)
    type = models.CharField(max_length=255, choices=REPORT_TYPE_CHOICES, default=AGGREGATE, null=True)
    frequency = models.CharField(max_length=255, choices=REPORT_FREQUENCY_CHOICES, default=DAILY, null=True)
    file_attachment = models.FileField(upload_to ='file_uploads/% Y/% m/% d/', null=True)
    file_attachment_data = models.BinaryField(null=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING, null=True) 

    description = models.TextField(null=True, blank=True)  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='myapp_report_created_by', null=True) 
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='myapp_report_updated_by', null=True, blank=True) 
    updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True, blank=True)
    
    # def __str__(self):
    #     return self.description
    class Meta:
        ordering = ['date']