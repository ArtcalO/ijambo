from django.db import models

# Create your models here.
class Eleve(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=25)