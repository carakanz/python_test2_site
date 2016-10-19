from __future__ import unicode_literals
from django.db import models
from personal_area.models import user
from core.models import dish
# Create your models here.

class order(models.Model):
    user = models.ForeignKey(user)
    date = models.DateField(auto_now_add=255)

    breakfast1 = models.ForeignKey(dish, related_name= 'breakfast1')
    dinner1 = models.ForeignKey(dish, related_name= 'dinner1')
    evening1 = models.ForeignKey(dish, related_name= 'evening1')
    breakfast2 = models.ForeignKey(dish, related_name= 'breakfast2')
    dinner2 = models.ForeignKey(dish, related_name= 'dinner2')
    evening2 = models.ForeignKey(dish, related_name= 'evening2')
    breakfast3 = models.ForeignKey(dish, related_name= 'breakfast3')
    dinner3 = models.ForeignKey(dish, related_name= 'dinner3')
    evening3 = models.ForeignKey(dish, related_name= 'evening3')
    breakfast4 = models.ForeignKey(dish, related_name= 'breakfast4')
    dinner4 = models.ForeignKey(dish, related_name= 'dinner4')
    evening4 = models.ForeignKey(dish, related_name= 'evening4')
    breakfast5 = models.ForeignKey(dish, related_name= 'breakfast5')
    dinner5 = models.ForeignKey(dish, related_name= 'dinner5')
    evening5 = models.ForeignKey(dish, related_name= 'evening5')
    breakfast6 = models.ForeignKey(dish, related_name= 'breakfast6')
    dinner6 = models.ForeignKey(dish, related_name= 'dinner6')
    evening6 = models.ForeignKey(dish, related_name= 'evening6')
    breakfast7 = models.ForeignKey(dish, related_name= 'breakfast7')
    dinner7 = models.ForeignKey(dish, related_name= 'dinner7')
    evening7 = models.ForeignKey(dish, related_name= 'evening7')
    tramsaction = models.BooleanField()