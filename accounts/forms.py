from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUserModel


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = CustomUserModel
        fields = (
            'phone',
            'name',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Passwords don't match"))

        return password2

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user


class CustomUserChangeFormInAdmin(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUserModel
        fields = (
            'phone', 'name', 'first_name', 'last_name', 'photo',
            'is_active', 'is_staff', 'is_superuser', 'is_verified',
            'otp', 'slug',
        )
