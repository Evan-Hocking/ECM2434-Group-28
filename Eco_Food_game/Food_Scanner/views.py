from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Food_Scanner import models
from users.models import Profile
from .itemRequest import itemAttributesDict
from .addItemPoints import isAdd, showPts, addPtsDB

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
    """ context = {'score': [{'ranking':scor.rank.rank , 'client': scor.userName, 'score':scor.score } for scor in Demo.objects.all().order_by('-userScore')]}
    d = Demo.objects.order_by('-userScore') """
    d = Profile.objects.order_by('-score')
    return render(request, 'Food_Scanner/leaderboard.html', locals())
    return render(request, 'Food_Scanner/leaderboard.html', locals())

def item(request):
    url = (request.get_full_path()).split("=")
    fragment = url[1]
    if isAdd(fragment):
        lib = showPts(fragment)
        # get data from db
        old_scor = Profile.objects.filter(user=request.user).first()
        if old_scor:
            old_scor.score = old_scor.score + score
            old_scor.save()
        else:
            Profile.objects.create(username=request.user, score=score)
        # update rank
        score_li = [score_obj.id for score_obj in Profile.objects.all().order_by('-score')]
        n = 1
        for i in score_li:
            userRank = Profile.objects.get(user_id=i)
            userRank.rank = n
            n = n + 1
        return JsonResponse({'status': 'sucess'})

        """ object = Profile.objects.filter(user=request.user).first()
        object.score = object.score + (int(lib['addPts']))
        addPtsDB(int(lib['addPts'])) """
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
