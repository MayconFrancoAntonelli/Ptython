
import pytz
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def getTimezone():
    return pytz.timezone(settings.TIME_ZONE)

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    
class Recipe (models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=160)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField(default='')
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True,default=None
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )
    def __str__(self):
        return self.title
