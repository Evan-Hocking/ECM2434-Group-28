from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

checkLogInStatus = False


def home(request):

    context = {
        'title': "HomePage",
        'loggedIn': checkLogInStatus
    }
    return render(request, 'Food_Scanner/home.html', context)


def about(request):
    context = {
        'title': "HomePage",
        'loggedIn': checkLogInStatus
    }
    return render(request, 'Food_Scanner/about.html', context)


def logIn(request):
    context = {
        'title': "Log-In Page",
        'loggedIn': checkLogInStatus
    }
    return render(request, 'Food_Scanner/logIn.html', context)


# def register(request):
#     context = {
#         'title': "Registration Page",
#         'loggedIn': checkLogInStatus
#     }
#     return render(request, 'Food_Scanner/register.html', context)


def leaderboard(request):
    context = {
        'title': "Leaderboard",
        'loggedIn': checkLogInStatus
    }
    return render(request, 'Food_Scanner/leaderboard.html', context)


def profile(request):
    context = {
        'title': "Profile Page",
        'loggedIn': checkLogInStatus
    }
    return render(request, 'Food_Scanner/profile.html', context)


def item(request):
    context = {
        'title': "Item Page",
        'loggedIn': checkLogInStatus
    }
    return render(request, 'Food_Scanner/item.html', context)

def addInfo_db(requst):
    models.Demo.objects.create(userScore = '10',userName = 'Testbot', userPw = '12345678', userEmail = '123456',role = 'Testbot')
    return HttpResponse('User has been added')
