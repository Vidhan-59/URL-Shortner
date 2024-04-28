from django.db import models
from django import forms
# Create your models here.
class url(models.Model):
    url1 = models.TextField(max_length=1000)