from django.shortcuts import render
from django.http import HttpResponse
from .models import Demo
import itemRequest

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

# def leaderboard(request):
#     context = {
#         'title': "Leaderboard",
#     }
#     return render(request, 'Food_Scanner/leaderboard.html', context)

def item(request):
    url = (request.get_full_path()).split("=")
    barcode = url[1]
    context = {
        'title': "Item Page",
        'barcode' : barcode,
    }
    return render(request, 'Food_Scanner/item.html', context)

def addInfo_db(requst):
    models.Demo.objects.create(userScore = '10',userName = 'Testbot', userPw = '12345678', userEmail = '123456',role = 'Testbot')
    return HttpResponse('User has been added')
