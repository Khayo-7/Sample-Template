# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from accounts.models import Account

# # from django.db import transaction
# # from django.conf import settings
# # from django.contrib import admin
# # from django.contrib.auth.forms import (UserCreationForm, UserChangeForm, AdminPasswordChangeForm)
# # from django.contrib.auth.models import User
# # from django.contrib import messages
# # from django.core.exceptions import PermissionDenied
# # from django.http import HttpResponseRedirect, Http404
# # from django.shortcuts import get_object_or_404
# # from django.template.response import TemplateResponse
# # from django.utils.html import escape
# # from django.utils.decorators import method_decorator
# # from django.utils.safestring import mark_safe
# # from django.utils.translation import ugettext, ugettext_lazy as _
# # from django.views.decorators.csrf import csrf_protect
# # from django.views.decorators.debug import sensitive_post_parameters



# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
# from copy import deepcopy


# class AccountAdmin(UserAdmin):
#     def get_fieldsets(self, request, obj=None):
#         fieldsets = super(UserAdmin, self).get_fieldsets(request, obj)
#         if not obj:
#             return fieldsets

#         if not request.user.is_superuser or request.user.pk == obj.pk:
#             fieldsets = deepcopy(fieldsets)
#             for fieldset in fieldsets:
#                 if 'is_staff' in fieldset[1]['fields']:
#                     if type(fieldset[1]['fields']) == tuple :
#                         fieldset[1]['fields'] = list(fieldset[1]['fields'])
#                     fieldset[1]['fields'].remove('is_staff')
#                     break

#         return fieldsets
#     list_display = ('user_ID','email','created_at', 'last_login')
#     search_fields = ('user_ID', 'email',)
#     readonly_fields=('created_at', 'last_login')

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

#     class Meta:
#         ordering =['user_ID']

# # User = get_user_model()
# # admin.site.unregister(User)
# # admin.site.register(User, UserAdmin)
# admin.site.register(Account, AccountAdmin)




# # csrf_protect_m = method_decorator(csrf_protect)

# # ### Unregister the existing User model from the admin
# # admin.site.unregister(User)

# # class UserAdmin(admin.ModelAdmin):
# #     add_form_template = 'admin/auth/user/add_form.html'
# #     change_user_password_template = None
# #     fieldsets = (
# #         (None, {'fields': ('username', 'password')}),

# #         (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),        

# #         ###################################
# #         #### CHANGE THIS RIGHT HERE #######        
# #         (_('Permissions'), {'fields': ('is_active', 'is_staff', 
# #                                        'groups', 'user_permissions')}),
# #         ####################################

# #         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
# #     )
# #     add_fieldsets = (
# #         (None, {
# #             'classes': ('wide',),
# #             'fields': ('username', 'password1', 'password2')}
# #         ),
# #     )
# #     form = UserChangeForm
# #     add_form = UserCreationForm
# #     change_password_form = AdminPasswordChangeForm
# #     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
# #     list_filter = ('is_staff', 'is_superuser', 'is_active')
# #     search_fields = ('username', 'first_name', 'last_name', 'email')
# #     ordering = ('username',)
# #     filter_horizontal = ('user_permissions',)

# #     def get_fieldsets(self, request, obj=None):
# #         if not obj:
# #             return self.add_fieldsets
# #         return super(UserAdmin, self).get_fieldsets(request, obj)

# #     def get_form(self, request, obj=None, **kwargs):
# #         """
# #         Use special form during user creation
# #         """
# #         defaults = {}
# #         if obj is None:
# #             defaults.update({
# #                 'form': self.add_form,
# #                 'fields': admin.util.flatten_fieldsets(self.add_fieldsets),
# #             })
# #         defaults.update(kwargs)
# #         return super(UserAdmin, self).get_form(request, obj, **defaults)

# #     def get_urls(self):
# #         from django.conf.urls import patterns
# #         return patterns('',
# #             (r'^(\d+)/password/$',
# #              self.admin_site.admin_view(self.user_change_password))
# #         ) + super(UserAdmin, self).get_urls()

# #     @sensitive_post_parameters()
# #     @csrf_protect_m
# #     @transaction.commit_on_success
# #     def add_view(self, request, form_url='', extra_context=None):
# #         # It's an error for a user to have add permission but NOT change
# #         # permission for users. If we allowed such users to add users, they
# #         # could create superusers, which would mean they would essentially have
# #         # the permission to change users. To avoid the problem entirely, we
# #         # disallow users from adding users if they don't have change
# #         # permission.
# #         if not self.has_change_permission(request):
# #             if self.has_add_permission(request) and settings.DEBUG:
# #                 # Raise Http404 in debug mode so that the user gets a helpful
# #                 # error message.
# #                 raise Http404(
# #                     'Your user does not have the "Change user" permission. In '
# #                     'order to add users, Django requires that your user '
# #                     'account have both the "Add user" and "Change user" '
# #                     'permissions set.')
# #             raise PermissionDenied
# #         if extra_context is None:
# #             extra_context = {}
# #         defaults = {
# #             'auto_populated_fields': (),
# #             'username_help_text': self.model._meta.get_field('username').help_text,
# #         }
# #         extra_context.update(defaults)
# #         return super(UserAdmin, self).add_view(request, form_url,
# #                                                extra_context)

# #     @sensitive_post_parameters()
# #     def user_change_password(self, request, id, form_url=''):
# #         if not self.has_change_permission(request):
# #             raise PermissionDenied
# #         user = get_object_or_404(self.queryset(request), pk=id)
# #         if request.method == 'POST':
# #             form = self.change_password_form(user, request.POST)
# #             if form.is_valid():
# #                 form.save()
# #                 msg = ugettext('Password changed successfully.')
# #                 messages.success(request, msg)
# #                 return HttpResponseRedirect('..')
# #         else:
# #             form = self.change_password_form(user)

# #         fieldsets = [(None, {'fields': form.base_fields.keys()})]
# #         adminForm = admin.helpers.AdminForm(form, fieldsets, {})

# #         context = {
# #             'title': _('Change password: %s') % escape(user.username),
# #             'adminForm': adminForm,
# #             'form_url': mark_safe(form_url),
# #             'form': form,
# #             'is_popup': '_popup' in request.REQUEST,
# #             'add': True,
# #             'change': False,
# #             'has_delete_permission': False,
# #             'has_change_permission': True,
# #             'has_absolute_url': False,
# #             'opts': self.model._meta,
# #             'original': user,
# #             'save_as': False,
# #             'show_save': True,
# #         }
# #         return TemplateResponse(request, [
# #             self.change_user_password_template or
# #             'admin/auth/user/change_password.html'
# #         ], context, current_app=self.admin_site.name)

# #     def response_add(self, request, obj, post_url_continue='../%s/'):
# #         """
# #         Determines the HttpResponse for the add_view stage. It mostly defers to
# #         its superclass implementation but is customized because the User model
# #         has a slightly different workflow.
# #         """
# #         # We should allow further modification of the user just added i.e. the
# #         # 'Save' button should behave like the 'Save and continue editing'
# #         # button except in two scenarios:
# #         # * The user has pressed the 'Save and add another' button
# #         # * We are adding a user in a popup
# #         if '_addanother' not in request.POST and '_popup' not in request.POST:
# #             request.POST['_continue'] = 1
# #         return super(UserAdmin, self).response_add(request, obj,
# #                                                    post_url_continue)

# # admin.site.register(User, UserAdmin)



# ###################3


# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from .forms import UserAdminCreationForm, UserAdminChangeForm

# User = get_user_model()

# # Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)

# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ['email', 'admin']
#     list_filter = ['admin']
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ()}),
#         ('Permissions', {'fields': ('admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ['email']
#     ordering = ['email']
#     filter_horizontal = ()


# admin.site.register(User, UserAdmin)