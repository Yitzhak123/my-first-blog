
from django import forms
from .models import DesktopUser
from .models import DesktopUserManager
from django.contrib.auth.models import User

class DesktopUserManagerForm(forms.ModelForm):

    class Meta:
        model = DesktopUserManager
        fields = ('username', 'email', 'password', )

class DesktopUserForm(forms.ModelForm):

    class Meta:
        model = DesktopUser
        fields = ('username', 'age', )