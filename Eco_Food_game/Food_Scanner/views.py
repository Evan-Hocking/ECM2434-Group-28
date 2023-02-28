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
    context = {'score': [{'ranking':scor.rank.rank , 'client': scor.userName, 'score':scor.score } for scor in Demo.objects.all().order_by('-userScore')]}
    d = Demo.objects.order_by('-userScore')
    return render(request, 'Food_Scanner/leaderboard.html', locals())

def item(request):
    context = {
        'title': "Item Page",
    }
    return render(request, 'Food_Scanner/item.html', context)


