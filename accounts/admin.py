from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from accounts.forms import CustomUserChangeFormInAdmin, CustomUserCreationForm
from accounts.models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    #   Форма редактирования пользователя
    form = CustomUserChangeFormInAdmin
    #   Форма создания пользователя
    add_form = CustomUserCreationForm

    #   Отображение полей на главном экране класса приложения
    list_display = (
        'phone', 'name', 'full_name', 'photo', 'is_active',
        'is_staff', 'is_superuser', 'is_verified', 'slug',
    )
    #   Поля-ссылки, для перехода к редактированию и просмотру определённого пользователя
    list_display_links = (
        'phone', 'name', 'slug',
    )
    #   Поля, по которым можно фильтровать пользователей
    list_filter = (
        'is_staff', 'is_verified',
    )
    #   Поля, отображаемые при переходе к редактированию
    #   и просмотру пользователя
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'photo')}),
        (_('Personal info'), {'fields': ('phone', 'name', 'slug')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Verification'), {'fields': ('otp', 'is_verified')}),
    )
    #   Поля, отображаемые при создании пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'name', 'password1', 'password2'),
        }),
    )
    #   Поля, по которым можно искать конкретного пользователя
    search_fields = (
        'phone',
        'name',
    )
    #   Поле, по которому упорядочивается список пользователей
    ordering = (
        'name',
    )
    filter_horizontal = (

    )


#   Регистрация модели в админка
admin.site.register(CustomUserModel, CustomUserAdmin)
#   Удаление Групп из админки
admin.site.unregister(Group)
