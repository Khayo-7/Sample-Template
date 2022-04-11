from django import forms
from django.forms import ModelForm

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from users.models import *
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('created_by', 'updated_by', )

class GroupForm(forms.ModelForm):
    
    class Meta:
        model = Group
        exclude = ('created_by', 'updated_by', )

class ContentForm(forms.ModelForm):
    
    class Meta:
        model = Content
        exclude = ('created_by', 'updated_by', )

class PermissionForm(forms.ModelForm):
    
    class Meta:
        model = Permission
        exclude = ('created_by', 'updated_by', )

class LevelForm(forms.ModelForm):
    
    class Meta:
        model = Level
        exclude = ('created_by', 'updated_by', ) 
        
class RoleForm(forms.ModelForm):
    
    class Meta:
        model = Role
        exclude = ('created_by', 'updated_by', )        

# class UserGroupForm(forms.ModelForm):
#     class Meta:
#         model = UserGroup
#         exclude = ('created_by', 'updated_by', )

# class UserRoleForm(forms.ModelForm):
#     class Meta:
#         model = UserRole
#         exclude = ('created_by', 'updated_by', )

# class GroupRoleForm(forms.ModelForm):
#     class Meta:
#         model = GroupRole
#         exclude = ('created_by', 'updated_by', )


# class CreateUserForm(forms.ModelForm):
#     # password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
#     # password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
#     # password2 = forms.CharField(widget = forms.HiddenInput(), max_length=255)
#     # password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = user
#         fields = '__all__' 
#         # forms.fields['password'].widget = forms.HiddenInput()
    
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if len(password) < 8:
#             raise ValidationError("the password is too short(< 8)")
#         return password

# class EntryForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
        
# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("email",)

# class RegisterForm(forms.ModelForm):
#     """
#     The default 

#     """

#     password = forms.CharField(widget=forms.PasswordInput)
#     password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['email']

#     def clean_email(self):
#         '''
#         Verify email is available.
#         '''
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("email is taken")
#         return email

#     def clean(self):
#         '''
#         Verify both passwords match.
#         '''
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_2 = cleaned_data.get("password_2")
#         if password is not None and password != password_2:
#             self.add_error("password_2", "Your passwords must match")
#         return cleaned_data
