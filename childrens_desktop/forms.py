
from django.utils.translation import ugettext_lazy

from django import forms
from .models import DesktopUser
from .models import DesktopUserManager
from .models import Movie


class DesktopUserManagerForm(forms.ModelForm):

    class Meta:
        model = DesktopUserManager
        fields = ('username', 'email', 'password', )


class DesktopUserForm(forms.ModelForm):

    class Meta:
        model = DesktopUser
        fields = ('username', 'age', )


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('name', 'min_age', )