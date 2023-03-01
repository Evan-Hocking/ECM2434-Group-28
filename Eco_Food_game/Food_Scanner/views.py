from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Food_Scanner import models
from Food_Scanner.models import Demo, Score
from .itemRequest import itemAttributesDict
from .addItemPoints import isAdd, showPts#, addPtsDB

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
    url = (request.get_full_path()).split("=")
    fragment = url[1]
    if isAdd(fragment):
        lib = showPts(fragment)
        # addPtsDB(lib['addPts'])
    else:
        lib = itemAttributesDict(fragment)

    context = {
        'title': "Item Page",
        'name' : lib['itemName'],
        'ecoRating' : lib['itemEcoR'],
        'energy' : lib['itemEner'],
        'nutri' : lib['itemNutr'],
        'proc' : lib['itemProc'],
        'imageLink' : lib['itemImg'],
        'score' : lib['itemScore'],
        'isError' : lib['isError'],
        'errorMsg' : lib['errorMsg'],
        'isAdd' : lib['isAdd'],
        'addPts' : lib['addPts'],
    }

    return render(request, 'Food_Scanner/item.html', context)
