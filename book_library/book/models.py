from django.db import models

# Create your models here.
class Book(models.Model):
  namebook = models.CharField(max_length=255)
  autor = models.CharField(max_length=255)