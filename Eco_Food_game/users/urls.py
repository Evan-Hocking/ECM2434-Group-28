#-------------------------------------------------------------------------------------------------------
# Name:        urls.py
# Purpose:     Declare the Urlpatterns so that the webpage request can be redirected to the correct page
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------------------------------

from django.urls import path
from django.contrib.auth import views as authViews
from . import views

#Declare the paths for each html webpage
urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'),
         name='auth-login'),
    path('logout/', authViews.LogoutView.as_view(template_name='users/logout.html'),
         name='auth-logout'),
    path('profile/', views.profile, name='user-profile'),
    path('profile/profile_update', views.profileUpdate, name='user-profile_update'),
    path('password/', authViews.PasswordChangeView.as_view(
        template_name='users/password.html', success_url='../profile'), name='update_password'),
    path('password-reset/',
         authViews.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         authViews.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         authViews.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         authViews.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('profile_list/', views.profile_list, name='profile_list'),
]
