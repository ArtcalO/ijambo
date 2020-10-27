from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . models import*
from . forms import*
# Create your views here.

def album(request):
	album_form = AlbumForm(request.POST or None,request.FILES)
	if(request.method =='POST'):
		if(album_form.is_valid()):
			album_form.save()
	album_form = AlbumForm()
	return render(request,"forms.html",locals())

def chanson(request):
	chanson_form = Chanson_du_moisForm(request.POST or None ,request.FILES)
	if(request.method =='POST'):
		if(chanson_form.is_valid()):
			chanson_form.save()
	chanson_form = Chanson_du_moisForm()
	return render(request,"forms.html",locals())




