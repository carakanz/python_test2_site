from __future__ import unicode_literals
from django.db import models

# Create your models here.
class user(models.Model):
    login = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length = 255)
    telephone = models.CharField(max_length = 30)
    count_order = models.IntegerField()
    description = models.TextField()
    fats = models.IntegerField()
    proteins = models.IntegerField()
    carbohydrates = models.IntegerField()
    calories = models.IntegerField()
    dairy = models.BooleanField()
    egg = models.BooleanField()
    gluten = models.BooleanField()
    peanut = models.BooleanField()
    seafood = models.BooleanField()
    sesame = models.BooleanField()
    soy = models.BooleanField()
    sulfite = models.BooleanField()
    tree_nut = models.BooleanField()
    wheat = models.BooleanField()
    last_authorization_day = models.DateField(auto_now_add=255)
    registration_day = models.DateField(auto_now_add=255)