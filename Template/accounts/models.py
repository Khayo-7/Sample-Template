# # from django.db import models
# # from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# # class MyAccountManager(BaseUserManager):
# # 	def create_user(self, email, username, password=None):
# # 		if not email:
# # 			raise ValueError('Users must have an email address')
# # 		if not username:
# # 			raise ValueError('Users must have a username')

# # 		user = self.model(
# # 			email=self.normalize_email(email),
# # 			username=username,
# # 		)

# # 		user.set_password(password)
# # 		user.save(using=self._db)
# # 		return user

# # 	def create_superuser(self, email, username, password):
# # 		user = self.create_user(
# # 			email=self.normalize_email(email),
# # 			password=password,
# # 			username=username,
# # 		)
# # 		user.is_admin = True
# # 		user.is_staff = True
# # 		user.is_superuser = True
# # 		user.save(using=self._db)
# # 		return user


# # class Account(AbstractBaseUser):
# # 	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
# # 	username 				= models.CharField(max_length=30, unique=True)
# # 	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
# # 	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
# # 	is_admin				= models.BooleanField(default=False)
# # 	is_active				= models.BooleanField(default=True)
# # 	is_staff				= models.BooleanField(default=False)
# # 	is_superuser			= models.BooleanField(default=False)


# # 	USERNAME_FIELD = 'email'
# # 	REQUIRED_FIELDS = ['username']

# # 	objects = MyAccountManager()

# # 	def __str__(self):
# # 		return self.email

# # 	# For checking permissions. to keep it simple all admin have ALL permissons
# # 	def has_perm(self, perm, obj=None):
# # 		return self.is_admin

# # 	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
# # 	def has_module_perms(self, app_label):
# # 		return True














# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class MyAccountManager(BaseUserManager):

#     def create_user(self, user_ID, email, password=None):
#         if not user_ID:
#             raise ValueError("Users must have a user ID")
#         if not email:
#             raise ValueError("Users must have an email address")

#         user = self.model(user_ID=user_ID, email=self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, user_ID, email, password):
#         user = self.create_user(
#             user_ID=user_ID,  
#             email=self.normalize_email(email),
#             password=password,
#         )
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class Account(AbstractBaseUser):
#     user_ID = models.CharField(max_length=30, unique=True)
#     first_name = models.CharField(max_length=255, default='First Name', null=True)
#     middle_name = models.CharField(max_length=255, default='Middle Name', null=True)
#     last_name = models.CharField(max_length=255, default='Last Name', editable=False, null=True)
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True, null=True)  
#     password = models.CharField(max_length=255, default='Password', null=True)
#     role = models.CharField(max_length=255, null=True)
#     is_superuser = models.BooleanField(default=False, null=True)
#     created_by = models.ForeignKey('self', on_delete=models.CASCADE, related_name='user_created_by', null=True) 
#     updated_by = models.ForeignKey('self', on_delete=models.CASCADE, related_name='user_updated_by', null=True) 
#     created_at = models.DateTimeField('Created Time', auto_now_add=True, null=True)
#     updated_at = models.DateTimeField('Last Updated Time', auto_now=True, null=True)
#     last_loggin = models.DateTimeField('Last Loggin Time', auto_now=True, null=True)
    

#     USERNAME_FIELD = 'user_ID'
#     REQUIRED_FIELDS = ['email', 'password']

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.first_name + self.middle_name
    
#     def has_permission(self, perm, obj=None):
#         return self.role

#     def has_module_permissions(self, app_label):
#         return self.role
####################################################

# from django.db import models
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )


# class User(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     is_active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False) # a admin user; non super-user
#     admin = models.BooleanField(default=False) # a superuser

#     # notice the absence of a "Password field", that is built in.

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [] # Email & Password are required by default.

#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email

#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff

#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_staffuser(self, email, password):
#         """
#         Creates and saves a staff user with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user

# # hook in the New Manager to our Model
# class User(AbstractBaseUser): # from step 2
#     ...
#     objects = UserManager()