from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from Food_Scanner import models
from django.shortcuts import HttpResponse

def home(request):
    return render(request, 'Food_Scanner/home.html')

def about(request):
    return render (request, 'Food_Scanner/about.html')

def addInfo_db(requst):
    models.Demo.objects.create(userScore = '10',userName = 'Testbot', userPw = '12345678', userEmail = '123456',role = 'Testbot')
    return HttpResponse('User has been added')