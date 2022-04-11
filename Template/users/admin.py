from django.contrib import admin
    
from .models import * 

# Register your models here.

# admin.site.register(profile)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Content)
admin.site.register(Permission)
admin.site.register(Level)
admin.site.register(Role)
# admin.site.register(UserRole)
# admin.site.register(GroupRole)
# admin.site.register(UserGroup)
admin.site.register(Log)