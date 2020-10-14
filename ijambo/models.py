from django.db import models
class Societe(models.Model):
	nom_societe = models.CharField(max_length=30)
	pays = models.CharField(max_length=15)

	def __str__(self):
		return f" {self.nom_societe} "
