from django.shortcuts import render
from django.http import HttpResponse
from .models import Demo
from .openFoodFactsPull import getProduct

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
    itemDict = getProduct(barcode)
    errorMsg = ""
    isError = False
    if isinstance(itemDict, str):
        errorMsg = "Error: Product not found"
        isError = True
        itemName = "N/A"
        itemEcoR = "N/A"
        itemEner = "N/A"
        itemNutr = "N/A"
        itemImg = "N/A"
        itemProc = "N/A"
    else:
        itemName = itemDict['name']
        itemEcoR = (itemDict['ecoRating']).upper()
        itemEner = itemDict['energy']
        itemNutr = (itemDict['nutriscore']).upper()
        itemImg = itemDict['image']
        itemProc = itemDict['processed']
        if itemProc.startswith("en"):
            itemProcStr = (itemDict['processed']).split(":")
            itemProcStr2 = (itemProcStr[1]).split("-")
            itemProc = itemProcStr2[0]

    if itemEcoR == "A":
        itemScore = 25
    elif itemEcoR == "B":
        itemScore = 15
    elif itemEcoR == "C":
        itemScore = 8
    elif itemEcoR == "D":
        itemScore = 4
    else:
        itemScore = 1

    context = {
        'title': "Item Page",
        'barcode' : itemDict,
        'name' : itemName,
        'ecoRating' : itemEcoR,
        'energy' : itemEner,
        'nutri' : itemNutr,
        'proc' : itemProc,
        'imageLink' : itemImg,
        'score' : itemScore,
        'isError' : isError,
        'errorMsg' : errorMsg,
    }
    return render(request, 'Food_Scanner/item.html', context)

def addInfo_db(requst):
    models.Demo.objects.create(userScore = '10',userName = 'Testbot', userPw = '12345678', userEmail = '123456',role = 'Testbot')
    return HttpResponse('User has been added')
