
from django.utils.translation import ugettext_lazy

from django import forms
from .models import DesktopUser
from .models import DesktopUserManager
from .models import Movie
from .models import Game


class DesktopUserManagerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = DesktopUserManager
        fields = ('username', 'email', 'password', )


class DesktopUserForm(forms.ModelForm):

    class Meta:
        model = DesktopUser
        fields = ('username', 'age', )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'user_username'}),
            'age': forms.TextInput(attrs={'class': 'user_age'}),
        }


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('name', 'min_age', )


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('name', 'min_age')