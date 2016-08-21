
from django import forms
from .models import DeskTopUserManager
from .models import DeskTopUserManagerLoginDetails

class DeskTopUserManagerLoginDetailsForm(forms.ModelForm):

    class Meta:
        model = DeskTopUserManagerLoginDetails
        fields = ('email', 'password', 'description')

class DeskTopUserManagerForm(forms.ModelForm):

    class Meta:
        model = DeskTopUserManager
        fields = ('name', 'email', 'password', )