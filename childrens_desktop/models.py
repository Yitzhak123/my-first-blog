import json

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Movie(models.Model):
    name = models.CharField(max_length=30)
    Movie_Category = (
        ('History' 'History'),
        ('Drama', 'Drama'),
        ('Fantazi', 'Fantazi'),
        ('None', 'None')
    )

    min_age = models.IntegerField()
    max_age = models.IntegerField()
    price = models.FloatField()

class DeskTopUser(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=60, primary_key=True)

    #applications =
    movies = models.TextField(null=False)
    games = models.TextField(null=False)

    def add_user(self, name, password, email):
        jsonDec = json.JSONDecoder()
        self.movies = json.dumps([])
        self.games = json.dumps([])
        self.save()

    def add_movie(self):
        
