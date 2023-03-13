from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Food_Scanner import models
from users.models import Profile
from .itemRequest import itemAttributesDict
from .addItemPoints import isAdd, showPts, addPtsDB, updateRank


def home(request):
    """
    Parse data to the homepage and render it from the provided template
    :param request: The pull request from the html
    :return: The Http response of the home page (home.html)
        type - Http Response obj
    """
    context = {
        'title': "HomePage",
    }
    return render(request, 'Food_Scanner/home.html', context)


def about(request):
    """
    Parse data to the about page and render it from the provided template
    :param request: The pull request from the html
    :return: The Http response of the about page (about.html)
        type - Http Response obj
    """
    context = {
        'title': "HomePage",
    }
    return render(request, 'Food_Scanner/about.html', context)


def leaderboard(request):
    """
    Gets an ordered list to the leaderboard page by descending order by score
    :param request: The pull request from the html
    :return: leaderboard.html & list variable connect with Profile database ordered DESC by score
        type - Http Response obj
    """
    '''Users profile from user.models table loaded into d and ordered DESC by score '''
    d = Profile.objects.order_by('-score')
    return render(request, 'Food_Scanner/leaderboard.html', locals())


def item(request):
    """
    Parse data to the item page and render it from the provided template
    :param request: The pull request from the html and barcode
    :return: item.html and eco Score and add it to user score in database and rank update
        type - Http Respone obj
    """
    # Gets header contents and splits into 2 lists, the value of the query (fragment),
    # and the rest of the URL, discards the rest of the url as it is not useful
    url = (request.get_full_path()).split("=")
    fragment = url[1]

    # Checks if the value of the fragment is an Add points request, not a barcode...
    if isAdd(fragment):
        # Breaks the url fragment down and returns a library of n/a except isAdd and addPts 
        lib = showPts(fragment)
        points = int(lib['addPts'])

        # Adds points of object to DB
        addPtsDB(request, points)

        # Updates users ranks according to updated scores
        updateRank()

    # ... Else the barcode is in URL (meaning the user has not yet chosen to add points this run)
    else:
        lib = itemAttributesDict(fragment)

    # Creates a dictionary
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
