from django.contrib import admin
from django.contrib.auth import views as authViews
from django.urls import path, include
from users import views as userViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', userViews.register, name='user-register'),
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'),
         name='auth-login'),
    path('logout/', authViews.LogoutView.as_view(template_name='users/logout.html'),
         name='auth-logout'),
    path('profile/', userViews.profile, name='user-profile'),
    path('', include('Food_Scanner.urls')),
]
