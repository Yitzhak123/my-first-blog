import json

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# The function get jsonlist, and add the object obj to jsonlist.
# It returns the new jsonlist
def add_object_to_jsonlist(jsonlist, obj):
	jsonDec = json.JSONDecoder()
	list = jsonDec.decode(jsonlist)
	list.append(obj)
	jsonlist = json.dumps(list)
	return jsonlist

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
    age = models.IntegerField(default=0)
    # List of applications types
    movies = models.TextField(null=False)
    games = models.TextField(null=False)

    def add_user(self):
        self.movies = json.dumps([])
        self.games = json.dumps([])
        self.save()

    def add_app(self, app_type, app_name):
        jsonlist_app_type = getattr(self, app_type)
        jsonlist_app_type = add_object_to_jsonlist(jsonlist_app_type, app_name)
        setattr(self, app_type, jsonlist_app_type)

class DesktopUserManager(DesktopUser):

    password = models.CharField(max_length=20)
    email = models.CharField(max_length=60, default="noEmail", unique=True)

    desktop_users_group = models.TextField(default="[]") # List of users

    def add_user_manager(self):
        self.desktop_users_group = json.dumps([])
        self.add_user()
        User.objects.create_user(
            username=self.username, email=self.email, password=self.password)

    def add_user_to_group(self, username):
        self.desktop_users_group = add_object_to_jsonlist(
                self.desktop_users_group, username)
        self.save()
