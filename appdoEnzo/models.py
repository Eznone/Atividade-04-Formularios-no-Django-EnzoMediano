from django.db import models

# Create your models here.

class Lived(models.Model):
  titulo = models.CharField(max_length = 50)
  country = models.CharField(max_length = 50)
  state = models.CharField(max_length = 50)
  years = models.CharField(max_length = 20)
  

class Schools(models.Model):
  name = models.CharField(max_length = 50)
  LEVEL = [
    ("Elementary", "E"),
    ("Middle", "M"),
    ("High", "H"),
    ("University", "U")
  ]
  level = models.CharField(max_length = 20, choices = LEVEL)
  city = models.CharField(max_length = 50)
  country = models.CharField(max_length = 50)
  state = models.CharField(max_length = 50)
  