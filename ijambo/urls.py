from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='ijambo-index'),
    path('register/', views.register, name='ijambo-register'),
    path('login/', views.login, name="ijambo-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='ijambo-logout'),
]
