# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate

# from account.models import Account


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

#     class Meta:
#         model = Account
#         fields = ('email', 'username', 'password1', 'password2', )


# class AccountAuthenticationForm(forms.ModelForm):

# 	password = forms.CharField(label='Password', widget=forms.PasswordInput)

# 	class Meta:
# 		model = Account
# 		fields = ('email', 'password')

# 	def clean(self):
# 		if self.is_valid():
# 			email = self.cleaned_data['email']
# 			password = self.cleaned_data['password']
# 			if not authenticate(email=email, password=password):
# 				raise forms.ValidationError("Invalid login")


# class AccountUpdateForm(forms.ModelForm):

# 	class Meta:
# 		model = Account
# 		fields = ('email', 'username', )

# 	def clean_email(self):
# 		email = self.cleaned_data['email']
# 		try:
# 			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
# 		except Account.DoesNotExist:
# 			return email
# 		raise forms.ValidationError('Email "%s" is already in use.' % account)

# 	def clean_username(self):
# 		username = self.cleaned_data['username']
# 		try:
# 			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
# 		except Account.DoesNotExist:
# 			return username
# 		raise forms.ValidationError('Username "%s" is already in use.' % username)










# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import ReadOnlyPasswordHashField

# User = get_user_model()

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


# class UserAdminCreationForm(forms.ModelForm):
#     """
#     A form for creating new users. Includes all the required
#     fields, plus a repeated password.
#     """
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['email']

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

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user


# class UserAdminChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ['email', 'password', 'is_active', 'admin']

#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]





