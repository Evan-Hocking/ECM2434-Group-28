# --------------------------------------------------------------------------------------------
# Name: views.py
# Purpose: Uses requests from web pages to generate data to populate the page with context
#
# Author: Ryan Gascoigne-Jones, Phil, Evan Hocking, Tom Sturgeon
#--------------------------------------------------------------------------------------------
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Eco_Food_game.users.achievements import check25
from Food_Scanner import models
from users.models import Profile
from .forms import addImage
from .itemRequest import itemAttributesDict
from .addItemPoints import isAdd, maxScans, showPts, addPtsHistDB, updateRank
from .scanner import barcodeReader
from PIL import Image
from pathlib import Path
from .onCampus import isOnCampus




def home(request):
    """
    Parse data to the homepage and render it from the provided template
    :param request: The http request from the html
    :return: The Http response of the home page (home.html)
        type - Http Response object
    """

    #url = (request.get_full_path()).split("=")
    #fragment = url[1]

    # If the method of request is POST
    if request.method == 'POST':
        print("Test")
        # Create a form using the UserRegistrationForm method from users/forms.py
        form = addImage( request.POST, request.FILES)
        if form.is_valid():
            # If the form is valid, Save it then redirect to the login page
            print("Form is saving and valid")
            image_file = form.cleaned_data['image']
            file_name = image_file.name
            form.save()
            return redirect(reverse('Food_Scanner-upload_barcode')+'?filename='+file_name)
    else:
        print("Form not valid")
        form = addImage()


    context = {
        'title': "HomePage",
        'form': form
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
        check25(request, context['addPts'])
        return render(request, 'Food_Scanner/item.html', context)

    # If the barcode is in URL (meaning the user has not yet chosen to add points) then:
    else:
        u = Profile.objects.filter(user=request.user).first()
        # Library of all attributes of an item
        context = itemAttributesDict(fragment)

        tags = context['tags']
        for i in tags:
            if i == "snack":
                u.Snack = u.Snack + 1
                u.save()
            elif i == "drink":
                u.Drink = u.Drink + 1
                u.save()
            elif i == "fruit":
                u.Fruit = u.Fruit + 1
                u.save()
            elif i == "vegetables":
                u.Vegetable = u.Vegetable + 1
                u.save()
            elif i == "protein":
                u.Protein = u.Protein + 1
                u.save()

        return render(request, 'Food_Scanner/item.html', context)

@csrf_exempt
def upload_barcode(request):

    """
    Takes image directory and applies barcodeReader function to it,
    decoding the response to be used in the redirecting to item page
    :param request: The http request from the html
    :return: data for upload_barcode.html to render page 
        type - Http Respone object
    """
    url = (request.get_full_path()).split("=")
    fragment = url[1]
    #path = Path("../media/barcode_imgs/haribo_starmix_barcode.png/")

    path = Path("Eco_Food_game\\media\\barcode_imgs\\"+fragment)

    #cur_path = 

    img = Image.open(path)

    barcodeData = barcodeReader(path)
        
    ############### Send barcode num in GET request to item page ###############

    context = {
        'barcodeImg': img,
        'barcodeNum': barcodeData['barcodeNum'],
        'isBarcode': barcodeData['isBarcode']
    }

    return redirect(reverse('Food_Scanner-item') + '?barcodeNumber='+barcodeData['barcodeNum'].decode('utf-8'))

   


def dashboard(request):
    user = Profile.objects.filter(user=request.user).first()

    context = {
        'user':user
    }

    return render(request, 'Food_Scanner/dashboard.html', context)
