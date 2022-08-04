from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class tasks (models.Model):
    nombre = models.CharField(max_length=20)
    descripcion=models.CharField(max_length=50)