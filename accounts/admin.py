from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.models import UserProfile


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


User = get_user_model()
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
