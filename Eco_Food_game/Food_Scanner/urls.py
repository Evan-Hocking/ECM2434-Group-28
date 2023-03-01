from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='Food_Scanner-home'),
    path('about/', views.about, name='Food_Scanner-about'),
    path('leaderboard/', views.leaderboard, name='Food_Scanner-leaderboard'),
    path('item/', views.item, name='Food_Scanner-item'),
]
