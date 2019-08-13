from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms



class PasswordChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('password',)


class MyUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser',
              'user_permissions')
        widgets = {'user_permissions': forms.CheckboxSelectMultiple}