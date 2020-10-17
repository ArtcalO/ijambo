from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Eleve(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=25)