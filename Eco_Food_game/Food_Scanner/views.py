#--------------------------------------------------------------------------------------------
# Name: views.py
# Purpose: Uses requests from web pages to generate data to populate the page with context
#
# Author: Ryan Gascoigne-Jones, Phil
#--------------------------------------------------------------------------------------------
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Food_Scanner import models
from users.models import Profile
from .itemRequest import itemAttributesDict
from .addItemPoints import isAdd, showPts, addPtsHistDB, updateRank, maxScans
from .onCampus import isOnCampus


def home(request):
    """
    Parse data to the homepage and render it from the provided template
    :param request: The http request from the html
    :return: The Http response of the home page (home.html)
        type - Http Response object
    """
    context = {
        'title': "HomePage",
    }
    return render(request, 'Food_Scanner/home.html', context)


def about(request):
    """
    Parse data to the about page and render it from the provided template
    :param request: The http request from the html
    :return: The Http response of the about page (about.html)
        type - Http Response object
    """
    
    context = {
        'title': "HomePage",
    }
    return render(request, 'Food_Scanner/about.html', context)

def leaderboard(request):
    """
    Returns an ordered list to the leaderboard page in descending order by score
    :param request: The http request from the html
    :return: data for leaderboard.html to use to render page & list variable connected with Profile database ordered DESC by score
        type - Http Response object
    """
    
    '''Users profile from user.models table loaded into d and ordered DESC by score '''
    d = Profile.objects.order_by('-score')
    return render(request, 'Food_Scanner/leaderboard.html', locals())

def item(request):
    """
    Parse data to the item page and render it from the provided template
    Sends all attributes and data of an object or adds number of points to a users score
    :param request: The http request from the html
    :return: data for item.html to render page and add the items score to user score in 
            database and rank update
        type - Http Respone object
    """

    # Gets header contents and splits into 2 lists, the value of the query (fragment),
    # and the rest of the URL, discards the rest of the url as it is not useful
    url = (request.get_full_path()).split("=")
    fragment = url[1]

    # If the user has clicked add points button then:
    if isAdd(fragment):
        # Breaks the url fragment down and returns a library of n/a except isAdd and addPts 
        context = showPts(fragment)
        if not isOnCampus():
            context['addPts'] = 0

        if maxScans(request):
            print("noPoints")
            context['addPts'] = 0
            context['spam'] = True
        # Adds points of object to users DB and item to history DB
        addPtsHistDB(request, int(context['addPts']), str(context['itemName']))
        return render(request, 'Food_Scanner/item.html', context)

    # If the barcode is in URL (meaning the user has not yet chosen to add points) then:
    else:
        # Library of all attributes of an item
        context = itemAttributesDict(fragment)

    return render(request, 'Food_Scanner/item.html', context)

def dashboard(request):
    user = Profile.objects.filter(user=request.user).first()

    return render(request, 'Food_Scanner/dashboard.html', locals())
