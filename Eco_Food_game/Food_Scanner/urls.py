from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Food_Scanner-home'),
    path('about/', views.about, name='Food_Scanner-about'),
    path('logIn/', views.about, name='Food_Scanner-Login'),
    path('register/', views.about, name='Food_Scanner-register'),
    path('leaderboard/', views.about, name='Food_Scanner-leaderboard'),
    path('profile/', views.about, name='Food_Scanner-profile'),
    ]
