from django.db import models

class Music(models.Model):
	chanteur = models.CharField(max_length=20)

class Album(models.Model):

	titre = models.CharField(max_length=20)
	cover = models.ImageField(upload_to ="music/covers")
	music = models.ForeignKey(Music, on_delete = models.CASCADE)

	def __str__(self):
		return f"Titre : {self.titre} Cover : {self.cover} Music : {self.music.chanteur}"

class Chanson_du_mois(models.Model):

	channel = models.CharField(max_length=20)
	audio = models.ForeignKey(Music, on_delete = models.CASCADE)

	def __str__(self): 
		return f"Channel : {self.channel} Titre : {self.audio.chanteur}"


		


