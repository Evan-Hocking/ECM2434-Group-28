from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Food_Scanner import models
from users.models import Profile
from .itemRequest import itemAttributesDict
from .addItemPoints import isAdd, showPts, addPtsDB, updateRank

# Create your views here.

"""
Parse data to the homepage and render it from the provided template
@param request from html
@return home.html
"""


def home(request):
    context = {
        'title': "HomePage",
    }
    return render(request, 'Food_Scanner/home.html', context)


"""
Parse data to the about page and render it from the provided template
@param request from html
@return about.html
"""


def about(request):
    context = {
        'title': "HomePage",
    }
    return render(request, 'Food_Scanner/about.html', context)

"""
Returns an ordered list to the leaderboard page
@param request from html
@return leaderboard.html & list variable connect with Profile database ordered DESC by score
"""
def leaderboard(request):
    '''Users profile from user.models table loaded into d and ordered DESC by score '''
    d = Profile.objects.order_by('-score')
    return render(request, 'Food_Scanner/leaderboard.html', locals())


"""
Parse data to the item page and render it from the provided template
@param request from html + barcode
@return item.html + eco Score and add it to user socre in database + rank update
"""


def item(request):
    # Gets header contents and splits into 2 lists, the value of the query (fragment),
    # and the rest of the URL, discards the rest of the url as it is not useful
    url = (request.get_full_path()).split("=")
    fragment = url[1]

    # Checks if the value of the fragment is an Add points request, not a barcode
    if isAdd(fragment):
        # Breaks the url fragment down and returns a library of n/a except isAdd and addPts 
        lib = showPts(fragment)
        points = int(lib['addPts'])

        # Adds points of object to DB
        addPtsDB(request, points)

        # Updates users ranks according to updated scores
        updateRank()

    # If the barcode is in URL (meaning the user has not yet chosen to add points this runs
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
        'score' : lib['itemPoints'],
        'isError' : lib['isError'],
        'errorMsg' : lib['errorMsg'],
        'isAdd' : lib['isAdd'],
        'addPts' : lib['addPts'],
    }
    

    return render(request, 'Food_Scanner/item.html', context)

def dashboard(request):
    user = Profile.objects.filter(user=request.user).first()

    return render(request, 'Food_Scanner/dashboard.html', locals())
