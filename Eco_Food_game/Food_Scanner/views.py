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

# Returns an ordered list to the leaderboard page

"""
Parse data to leaderboard page and render it from the provided template
Sends a list of profiles including scores and usernames to be displayed
@param - request
    type - HttpRequest
    content - data about request made to leaderboard page
@return - render
    type - HttpResponse
    content - data for item page to use to render page
"""
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

"""
Parse data to the item page  (which is navigated to when user enters a barcode)
and render it from the provided template
Sends all attributes and data of an object or adds number of points to a users score
@param - request
    type - HttpRequest
    content - data about request made to item page
@return - render
    type - HttpResponse
    content - data for item page to use to render page
"""
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

    # If the user has clicked add points button then:
    if isAdd(fragment):
        # Breaks the url fragment down and returns a library of n/a except isAdd and addPts 
        context = showPts(fragment)
        points = int(context['addPts'])

        # Adds points of object to DB
        addPtsDB(request, points)

        # Updates users ranks according to updated scores
        updateRank()

    # If the barcode is in URL (meaning the user has not yet chosen to add points) then:
    else:
        # Library of all attributes of an item
        context = itemAttributesDict(fragment)

    return render(request, 'Food_Scanner/item.html', context)
