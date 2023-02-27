"""Eco_Food_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as authViews
from django.urls import path, include
from users import views as userViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',userViews.register, name='user-register'),
    path('login/',authViews.LoginView.as_view(template_name='users/login.html'), name='auth-login'),
    path('logout/',authViews.LogoutView.as_view(template_name='users/logout.html'), name='auth-logout'),
    path('profile/', userViews.profile, name='user-profile'),
    path('leaderboard/', userViews.leaderboard, name='user-leaderboard'),
    path('', include('Food_Scanner.urls')),
]
