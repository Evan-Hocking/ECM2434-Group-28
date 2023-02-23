from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Food_Scanner-home'),
    path('about/', views.about, name='Food_Scanner-about'),
    path('logIn/', views.logIn, name='Food_Scanner-Login'),
    path('register/', views.register, name='Food_Scanner-register'),
    path('leaderboard/', views.leaderboard, name='Food_Scanner-leaderboard'),
    path('profile/', views.profile, name='Food_Scanner-profile'),
    path('item/', views.item, name='Food_Scanner-item'),
]
