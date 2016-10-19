from __future__ import unicode_literals
from django.db import models
from personal_area.models import user
from core.models import dish

# Create your models here.
class comment(models.Model):
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=255)
    write_user = models.ForeignKey(user)
    comment_dish = models.ForeignKey(dish)