from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Food_Scanner import models
from Food_Scanner.models import Demo, Score
from .itemRequest import itemAttributesDict

# Create your views here.

"""
Parse data to the homepage and render it from the provided template
"""


def home(request):
    context = {
        'title': "HomePage",
    }
    return render(request, 'Food_Scanner/home.html', context)


"""
Parse data to the about page and render it from the provided template
"""


def about(request):
    context = {
        'title': "HomePage",
    }
    return render(request, 'Food_Scanner/about.html', context)


"""
Parse data to the leaderboard webpage and render it from the provided template
"""


def leaderboard(request):
    context = {'score': [{'ranking': scor.rank.rank, 'client': scor.userName,
                          'score': scor.score} for scor in Demo.objects.all().order_by('-userScore')]}
    d = Demo.objects.order_by('-userScore')
    return render(request, 'Food_Scanner/leaderboard.html', locals())


"""
Parse data to the item page and render it from the provided template
"""


def item(request):
    url = (request.get_full_path()).split("=")
    barcode = url[1]
    lib = itemAttributesDict(barcode)

    context = {
        'title': "Item Page",
        'name': lib['itemName'],
        'ecoRating': lib['itemEcoR'],
        'energy': lib['itemEner'],
        'nutri': lib['itemNutr'],
        'proc': lib['itemProc'],
        'imageLink': lib['itemImg'],
        'score': lib['itemScore'],
        'isError': lib['isError'],
        'errorMsg': lib['errorMsg'],
    }
    return render(request, 'Food_Scanner/item.html', context)
