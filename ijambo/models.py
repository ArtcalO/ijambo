from django.db import models
class Societe(models.Model):
	nom_societe = models.CharField(max_length=30)
	pays = models.CharField(max_length=15)

<<<<<<< HEAD
# Create your models here.
<<<<<<< HEAD
<<<<<<< HEAD
class Music(models.Model):
	Titre=models.TextField(max_length=200)
=======
	def __str__(self):
		return f" {self.nom_societe} "
>>>>>>> origin/Marley
=======
class Eleve(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=25)
>>>>>>> origin/shwaib
=======
class Eleve(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=25)
>>>>>>> origin/shwaib
