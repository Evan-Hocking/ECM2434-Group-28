from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    context = {
        'title': "HomePage"
    }
    return render(request, 'Food_Scanner/home.html', context)


def about(request):
    context = {
        'title': "HomePage"
    }
    return render(request, 'Food_Scanner/about.html', context)


def logIn(request):
    context = {
        'title': "Log-In Page"
    }
    return render(request, 'Food_Scanner/logIn.html', context)


def register(request):
    context = {
        'title': "Registration Page"
    }
    return render(request, 'Food_Scanner/register.html', context)


def leaderboard(request):
    context = {
        'title': "Leaderboard"
    }
    return render(request, 'Food_Scanner/leaderboard.html', context)


def profile(request):
    context = {
        'title': "Profile Page"
    }
    return render(request, 'Food_Scanner/profile.html', context)
