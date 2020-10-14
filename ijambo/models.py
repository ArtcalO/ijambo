from django.db import models

# Create your models here.
class Music(models.Model):
	Titre=models.TextField(maxlength=200)
