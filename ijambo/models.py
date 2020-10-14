from django.db import models

class Societe(models.Model):
	nom_societe = models.CharField(max_length=30)
	pays = models.CharField(max_length=15)

class Music(models.Model):
	Titre=models.TextField(max_length=200)

	def __str__(self):
		return f" {self.nom_societe} "

class Eleve(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=25)

class Eleve(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=25)

