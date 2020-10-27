from django import forms
from . models import *
class AlbumForm(forms.ModelForm):

	titre=forms.CharField(
		label='titre',
		widget = forms.TextInput(
			attrs = {

				'placeholder' :'Nom album',
				'class' : 'form-control'
			
				}
			))

		

	cover = forms.ImageField(
		label = 'cover',
		widget = forms.FileInput(
			attrs = {
				'class':'form-control'
				}
			))

	music = forms.ModelChoiceField(
		label = 'music',
		queryset = Music.objects.all(),
		widget = forms.Select(
			attrs = {
				'class' : 'form-control'
				}
			))


	class Meta :
		model = Album
		fields = '__all__'

class Chanson_du_moisForm(forms.ModelForm):
	channel = forms.CharField(
		label = 'ChannelName',
		widget = forms.TextInput(
			attrs = {

				'placeholder' : 'Nom du radio',
				'class' : 'form-control'
				}
			))


	audio= forms.ModelChoiceField(
		label = 'audio',
		queryset = Music.objects.all(),
		widget = forms.Select(
			attrs = {
				'class' : 'form-control'
				}
			))

	class Meta : 
		model = Chanson_du_mois
		fields = '__all__'










			





