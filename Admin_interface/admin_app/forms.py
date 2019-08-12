from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm



class PasswordChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('password',)
