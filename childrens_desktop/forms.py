
from django import forms
from .models import DesktopUser
from .models import DesktopUserManager
from .models import DesktopUserManagerLoginDetails
from django.contrib.auth.models import User

class DesktopUserManagerLoginDetailsForm(forms.ModelForm):

    class Meta:
        model = DesktopUserManagerLoginDetails
        fields = ('email', 'password', 'description')

class DesktopUserManagerForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )