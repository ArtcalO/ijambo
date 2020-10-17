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
			return redirect('ijambo-index')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', locals())