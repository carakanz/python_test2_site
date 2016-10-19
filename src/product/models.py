from __future__ import unicode_literals
from django.db import models

# Create your models here.
class product(models.Model):
    titele = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to=None, height_field=1000, width_field=200, max_length=100)
    description = models.TextField()
    cost = models.IntegerField()
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
    pub_date = models.DateField(auto_now_add=255)
    count = models.IntegerField()