from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from accounts.forms import CustomUserChangeFormInAdmin, CustomUserCreationForm
from accounts.models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeFormInAdmin
    add_form = CustomUserCreationForm

    list_display = (
        'phone', 'name', 'full_name', 'photo', 'is_active',
        'is_staff', 'is_superuser', 'is_verified', 'slug',
    )
    list_display_links = (
        'phone', 'name', 'slug',
    )
    list_filter = (
        'is_staff', 'is_verified',
    )
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'photo')}),
        ('Personal info', {'fields': ('phone', 'name', 'slug')}),
        ('Permission', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Verification', {'fields': ('otp', 'is_verified')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = (
        'phone',
        'name',
    )
    ordering = (
        'name',
    )
    filter_horizontal = (

    )


admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.unregister(Group)
