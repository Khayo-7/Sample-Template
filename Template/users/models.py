from django.db import models


TITLE_CHOICES = [
        ('MR', 'Mr.'),
        ('MRS', 'Mrs.'),
        ('MS', 'Ms.'),
]
# To be addressed

# User
#   Position
#   Role
#   Group
#       Level
#       Parent 

# User
# Level
#     Technical 0
#     Supervision 1
#     Team 2
#     Center 3
#     Division 4
#     Wing 5

# technical s

# m-sup1    M
# m-sup2    M
# i-sup1  I
# i-sup2    I
# Intrusion     Cert
# Malware   Cert
# soc   cert
# cti   cert
# Team5     C
# cert  D
# Center    D
# Division   Null

PROFESSIONAL = 'professional'
SUPERVISOR = 'supervisor'
TEAM_LEADER = 'team_leader'
CENTER_MANAGER = 'center_manager'
DIVISION_MANAGER = 'division_manager'
WING_MANAGER = 'wing_manager'

TECHNICAL = 'technical'
SUPERVISION = 'supervision'
TEAM = 'team'
CENTER = 'center'
DIVISION = 'division'
WING = 'wing'

ANALYST = 'analyst'
RESEARCHER = 'researcher'
DEVELOPER = 'developer'
SUPPORTING_STAFF = 'supporting_taff'

POSITION_CHOICES = [
        (PROFESSIONAL, 'Professional'),
        (SUPERVISOR, 'Supervisor'),
        (TEAM_LEADER, 'Team Leader'),
        (CENTER_MANAGER, 'Center Manager'),
        (DIVISION_MANAGER, 'Division Manager'),
        (WING_MANAGER, 'Wing Manager'),
]

LEVEL_CHOICES = [
        (TECHNICAL, 'Technical'),
        (SUPERVISION, 'Supervision'),
        (TEAM, 'Team'),
        (CENTER, 'Center'),
        (DIVISION, 'Division'),
        (WING, 'Wing'),
]

PROFESSIONAL_ROLE_CHOICES = [
        (ANALYST, 'Analyst'),
        (RESEARCHER, 'Researcher'),
        (DEVELOPER, 'Developer'),
        (SUPPORTING_STAFF, 'Supporting Staff'),
]

# Create your models here.

# class Profile(models.Model):
#     first_name = models.CharField(max_length=255, null=True)
#     middle_name = models.CharField(max_length=255, null=True)
#     last_name = models.CharField(max_length=255, editable=False, null=True)
# from phonenumber_field.modelfields import PhoneNumberField
#     phone = PhoneNumberField(null=False, blank=False, unique=True)
# #form
# from phonenumber_field.formfields import PhoneNumberField
# phone = PhoneNumberField()
# client.phone.as_e164 # get as string
# Normalization for testing 
# from phonenumber_field.phonenumber import PhoneNumber
# phone = PhoneNumber.from_string(phone_number=raw_phone, region='RU').as_e164
# form using regex
#  class ReceiverForm(forms.ModelForm):
#      phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
#                                      error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits is allowed."))
# from django.core.validators import RegexValidator

# class PhoneModel(models.Model):
#     ...
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
# pip install django-phonenumber-field
# pip install django-phone-field # lite version
# PHONENUMBER_DEFAULT_REGION = 'US'
#     address = models.CharField(max_length=255, null=True)
#     created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
#     updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True)
    
#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)
    
class User(models.Model):
    
    user_ID = models.CharField(unique=True, max_length=255)   
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True, null=True)
    password = models.CharField(max_length=255, null=True)

    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, blank=True)
    position = models.CharField(max_length=255, choices=POSITION_CHOICES, default=PROFESSIONAL, null=True)

    # last_name = models.CharField(max_length=255, editable=False, null=True)    
    # title = models.CharField(max_length=3, choices=TITLE_CHOICES, null=True)
    #role = models.CharField(max_length=255, null=True)  
    # profile = models.ForeignKey(profile, on_delete=models.CASCADE, null=True)
    # username = models.CharField(max_length=255, default='username', null=True)

    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='user_created_by', null=True) 
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='user_updated_by', null=True) 
    updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True)
    last_login = models.DateTimeField('Last Loggin Time', auto_now=True, null=True)
      
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Content(models.Model):
    app = models.CharField(max_length=255, null=True)
    model = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='content_created_by', null=True)  
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='content_updated_by', null=True)
    updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True)

    class Meta:
        unique_together = (("app", "model"),)
        
    def __str__(self):
        return "%s in module %s" % (self.model, self.app)
        
class Permission(models.Model):
    code = models.CharField(unique=True, max_length=255)
    name = models.CharField(unique=True, max_length=255, null=True)
    description = models.TextField(null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='permission_created_by', null=True)  
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='permission_updated_by', null=True)
    updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True)

    class Meta:
        unique_together = (("code", "name"),)

    def __str__(self):
        return "%s(%s)" % (self.name, self.code)
        
class Role(models.Model):
    code = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255, null=True)
    has_type = models.BooleanField(default=False)
    type = models.CharField(max_length=255, choices=PROFESSIONAL_ROLE_CHOICES, default=ANALYST, null=True)
    permission = models.ManyToManyField(Permission, related_name='role_permissions_created_by') 
    description = models.TextField(null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='role_created_by', null=True)  
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='arole_updated_by', null=True)
    updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True)

    class Meta:
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
        return "%s(%s)" % (self.name, self.code)
        
class Level(models.Model):
    code = models.CharField(unique=True, max_length=255)
    name = models.CharField(unique=True, max_length=255, null=True)
    description = models.TextField(null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='level_created_by', null=True)  
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='level_updated_by', null=True)
    updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True)

    class Meta:
        unique_together = (("code", "name"),)

    def __str__(self):
        return "%s(%s)" % (self.name, self.code)

class Group(models.Model):

    code = models.CharField(unique=True, max_length=255)
    name = models.CharField(unique=True, max_length=255, null=True)
    description = models.TextField(null=True)
    
    # member = models.ManyToManyField(User, blank=True)
    # level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    level = models.CharField(max_length=255, choices=LEVEL_CHOICES, default=TECHNICAL, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='group_parent', null=True) 

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='group_created_by', null=True)  
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='group_updated_by', null=True)
    updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True)

    class Meta:
        unique_together = (("code", "name"),)

    def __str__(self):
        return "%s(%s)" % (self.name, self.code)

# User
#   Position
#   Role
#   Group
#       Level
#       Parent 

# class UserGroup(models.Model):
#     member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

#     recruited_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='User_group_created_by', null=True) 
#     created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
#     updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='User_group_updated_by', null=True) 
#     updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True)

#     class Meta:
#         unique_together = (("group", "member"),)
        
#     def __str__(self):
#         return "%s in %s" % (self.member.user_ID, self.group.name)
        
# class UserRole(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='User_role_created_by', null=True) 
#     created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
#     updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='User_role_updated_by', null=True) 
#     updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True)
    
#     class Meta:
#         unique_together = (("user", "role"),)

#     def __str__(self):
#         return "%s can %s" % (self.user.user_ID, self.role.name)
        
# class GroupRole(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
#     role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='group_role_created_by', null=True) 
#     created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
#     updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='group_role_updated_by', null=True) 
#     updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True)
    
#     class Meta:
#         unique_together = (("group", "role"),)

#     def __str__(self):
#         return "%s can %s" % (self.group.name, self.role.name)
        
class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    content = models.ForeignKey(Content, on_delete=models.SET_NULL, null=True)
    activity = models.TextField(null=True)
    created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)

    def __str__(self):
        return "%s %s %s" % (self.user.user_ID, self.group.name, self.content)
        