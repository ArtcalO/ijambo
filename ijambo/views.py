from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import *
# Create your views here.

class HomeView(View):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, locals())

def register(request):
    	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid:
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('ijambo-login')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', locals())

def login(request):
	login_form = loginForm(request.POST)

	if request.method=='POST':
		
		if login_form.is_valid():
			email = login_form.cleaned_data['email']
			password = login_form.cleaned_data['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect('ijambo-index')
			else:
				login_form = loginForm()

	login_form = loginForm()
	return render(request, '', locals())