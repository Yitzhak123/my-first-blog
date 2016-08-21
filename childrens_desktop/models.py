import json

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AppModel(models.Model):
    name = models.CharField(max_length=30, default="???", unique=True)
    min_age = models.IntegerField(default=4)
    max_age = models.IntegerField(default=12)
    link_to_app = models.CharField(max_length=200, default="no link")

class Movie(AppModel):
    MOVIE_CATEGORY = (
        ('0', 'History'),
        ('1', 'Drama'),
        ('2', 'Fantazi'),
        ('3', 'NoCategory')
    )

    category = models.CharField(max_length=1, choices=MOVIE_CATEGORY, default='NoCategory')

class Game(AppModel):
    GAME_CATEGORY = (
        ('1', 'Strategy'),
        ('2', 'Action'),
        ('3', 'Racing')
    )

class DesktopUser(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=30, unique=True)
    # List of applications types
    movies = models.TextField(null=False)
    games = models.TextField(null=False)

    def add_user(self):
        self.movies = json.dumps([])
        self.games = json.dumps([])
        self.save()

    def add_app(self, app_type, app_name):
        jsonDec = json.JSONDecoder()
        list_app_type = jsonDec.decode(getattr(self, app_type))
        list_app_type.append(app_name)
        setattr(self, app_type, list_app_type)

class DesktopUserManager(DesktopUser):

    password = models.CharField(max_length=20)
    email = models.CharField(max_length=60, default="noEmail", unique=True)
    user = models.OneToOneField(User, default=None)

    desktop_users = models.TextField() # List of users

    def add_user_manager(self):
        self.add_user()
        User.objects.create(username=self.name, email=self.email, password=self.password)

class DesktopUserManagerLoginDetails(models.Model):
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    description = models.TextField(default="Email or password is incorrect")
