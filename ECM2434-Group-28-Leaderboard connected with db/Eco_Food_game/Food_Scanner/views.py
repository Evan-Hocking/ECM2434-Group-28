from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Food_Scanner import models
from Food_Scanner.models import Demo, Score


# Create your views here.

def home(request):
    context = {
        'title': "HomePage",
    }
    return render(request, 'Food_Scanner/home.html', context)


def about(request):
    context = {
        'title': "HomePage",
    }
    return render(request, 'Food_Scanner/about.html', context)


def leaderboard(request):
    d = Demo.objects.order_by('-userScore')
    return render(request, 'Food_Scanner/leaderboard.html', locals())

def item(request):
    context = {
        'title': "Item Page",
    }
    return render(request, 'Food_Scanner/item.html', context)


