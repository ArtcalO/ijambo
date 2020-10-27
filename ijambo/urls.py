from django.urls import path
from . import views
urlpatterns = [
    path('Album/',views.album,name="alb"),
    path('Chanson/',views.chanson,name="song")


]
