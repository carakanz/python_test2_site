from __future__ import unicode_literals
from django.db import models
from product.models import product
from personal_area.models import user
# Create your models here.

class dish(models.Model):
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    first_course_id = models.ForeignKey(product, related_name= 'first_course_id')
    second_course_id = models.ForeignKey(product, related_name= 'second_course_id')
    garnish_id = models.ForeignKey(product, related_name= 'garnish_id')
    salad_id = models.ForeignKey(product, related_name= 'salad_id')
    present = models.ForeignKey(product, related_name= 'present')
    pub_date = models.DateField(auto_now_add=255)
    user_id = models.ForeignKey(user)