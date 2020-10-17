from django import forms
from django.contrib.auth.forms import UserCreationForm

class loginForm(forms.Form):
    email = forms.EmailField(
		widget = forms.EmailInput(
			attrs ={
				'placeholder':'E-mail',
                'type':'email'
			}
		)
	) 
	password = forms.CharField(
		widget = forms.PasswordInput(
			attrs = {
				'placeholder':'Password',
				'type':'password',
				'class':'form-control'
			}
		)
	)