from django.urls import path
from . import views

"""
Define the url paths that each webpage follows
"""
urlpatterns = [
    path('', views.home, name='Food_Scanner-home'),
    path('about/', views.about, name='Food_Scanner-about'),
    path('leaderboard/', views.leaderboard, name='Food_Scanner-leaderboard'),
    path('item/', views.item, name='Food_Scanner-item'),
    path('dashboard/', views.dashboard, name='Food_Scanner-dashboard')
]
