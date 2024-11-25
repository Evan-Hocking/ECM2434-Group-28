#-------------------------------------------------------------------------------
# Name:        urls.py
# Purpose:     Defines the url paths that each webpage follows
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------
from django.urls import path
from . import views

# Defining the url paths that each webpage follows
urlpatterns = [
    path('', views.home, name='Food_Scanner-home'),
    path('about/', views.about, name='Food_Scanner-about'),
    path('leaderboard/', views.leaderboard, name='Food_Scanner-leaderboard'),
    path('item/', views.item, name='Food_Scanner-item'),
    path('upload_barcode', views.upload_barcode, name='Food_Scanner-upload_barcode'),
    path('dashboard/', views.dashboard, name='Food_Scanner-dashboard')
]
