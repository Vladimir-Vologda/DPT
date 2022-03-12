from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


def photo_dir(instance, filename):
    #   Функция, при которой сохранение файлов будет
    #   производиться в отдельную папку для каждого пользователя,
    #   папка создаётся по его 'name'
    return f'accounts/{instance.name}/{filename}'


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    phone = PhoneNumberField(_('Phone number'), unique=True, db_index=True)
    name = models.CharField(_('Username'), max_length=50, unique=True, db_index=True)
    first_name = models.CharField(_('Name'), max_length=50, blank=True)
    last_name = models.CharField(_('Surname'), max_length=50, blank=True)
    photo = models.ImageField(_('Photo'), upload_to=photo_dir, default='default/accounts_default.PNG')
    is_active = models.BooleanField(_('Status active'), default=True)
    is_staff = models.BooleanField(_('Status staff'), default=False)
    is_superuser = models.BooleanField(_('Status superuser'), default=False)
    is_verified = models.BooleanField(_('Verified'), default=False)
    otp = models.CharField(_('Verification code'), max_length=6)
    slug = models.SlugField(_('URL-address'), unique=True, db_index=True)

    #   Пользовательский менеджер
    objects = ''

    #   Обязательное поле, по которому пользователь будет входить в систему
    USERNAME_FIELD = 'phone'
    #   Дополнительные обязательные поля,
    #   которые вводятся при регистрации
    REQUIRED_FIELDS = ('name',)

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'{self.name} - {self.phone}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(CustomUserModel, self).save(*args, **kwargs)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
