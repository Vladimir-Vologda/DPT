from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, name, password, **extra_fields):
        """
        Создание и сохранение пользователя с указанными: телефоном, именем и паролем.
        """
        if not phone:
            raise ValueError(_('Phone number must be set'))

        if not name:
            raise ValueError(_('Name must be set'))

        user = self.model(
            phone=phone,
            name=name,
            **extra_fields
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, name, password=None, **extra_fields):
        """
        Создание пользователя.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, name, password, **extra_fields)

    def create_superuser(self, phone, name, password=None, **extra_fields):
        """
        Создание суперпользователя.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(phone, name, password, **extra_fields)
