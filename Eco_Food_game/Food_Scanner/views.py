from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Food_Scanner import models
from users.models import Profile
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

# Right now just returns an empty leaderboard with only thing being 5 blank users with rank 0
def leaderboard(request):
    """ context = {'score': [{'ranking':scor.rank.rank , 'client': scor.userName, 'score':scor.score } for scor in Demo.objects.all().order_by('-userScore')]}
    d = Demo.objects.order_by('-userScore') """
    # context = {'score': [{'ranking':scor.rank.rank , 'client': scor.userName, 'score':scor.score } for scor in Profile.objects.all().order_by('-userScore')]}
    d = Profile.objects.order_by('-score')
    return render(request, 'Food_Scanner/leaderboard.html', locals())

def item(request):
    # Gets header contents and splits into 2 lists, the value of the query (fragment),
    # and the rest of the URL
    url = (request.get_full_path()).split("=")
    fragment = url[1]

    # Checks if the value of the fragment is an Add points request, not a barcode
    if isAdd(fragment):
        # Breaks the url fragment down and returns a library of n/a except isAdd and addPts 
        lib = showPts(fragment)
        score = int(lib['addPts'])
        
        # Get data from db
        old_scor = Profile.objects.filter(user=request.user).first()
        if old_scor:
            old_scor.score = old_scor.score + score
            old_scor.save()
        else:
            Profile.objects.create(username=request.user, score=score)
        
        # Update rank
        # Commented out as it was causing error: profile does not 
        # exist on 'userRank = Profile.objects.get(user_id=i)'
        """ score_li = [score_obj.id for score_obj in Profile.objects.all().order_by('-score')]
        n = 1
        for i in score_li:
            userRank = Profile.objects.get(user_id=i)
            userRank.rank = n
            n = n + 1 """

        # To use if we want to put above code in a external module and func
        # addPtsDB(int(lib['addPts']))

        # Just in case we need to go back to
        """ object = Profile.objects.filter(user=request.user).first()
        object.score = object.score + (int(lib['addPts'])) """
        
    # If the barcode is in URL run this func
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
