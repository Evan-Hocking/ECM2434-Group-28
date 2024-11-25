#-------------------------------------------------------------------------------
# Name:        views.py
# Purpose:     Render the webpages for all pages to do with user information
#
# Author:      Tom Sturgeon
#-------------------------------------------------------------------------------
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login_required
#from Eco_Food_game.users.achievements import check25
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import History, Profile, Achievements
from .achievements import checkAchievements


def register(request):
    """
    Pass User registration form to the register webpage based on the register.html template
    :param request: The data about request made to webpage
        type - HttpRequest
    :return: The requested webpage based on the supplied template with context passed to it 
        type - HttpRequest or HttpResponseRedirect
    """
    # If the method of request is POST
    if request.method == 'POST':
        # Create a form using the UserRegistrationForm method from users/forms.py
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # If the form is valid, Save it then redirect to the login page
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You can now log in!')
            # Redirect to the login form
            return redirect('auth-login')
    else:
        # Sets to the register form
        form = UserRegisterForm()

    # Returns and render the webpage and pass the form into the template
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """
    Pass the profile information to the correct webpage
    You need to be logged in to access webpage otherwise you will be redirected to Food_Scanner-home 
    :param request: The data about request made to webpage
        type - HttpRequest
    :return: The requested webpage based on the supplied template with context passed to it
        type - HttpRequest
    """
    
    # Gets the current user profile
    curProfile = Profile.objects.get(user=request.user)

    # Collects history from database
    history = History.objects.filter(userId_id=curProfile.id).order_by('-date_Added')
    
    # Gets the users ordered by score
    profiles = Profile.objects.order_by('-score')
    
    # Checks the achievements of the user profile
    checkAchievements(request)
    achievements = Achievements.objects.all()

    for x in range(0,len(achievements)):
        # Checking that achievements and user matches
        if achievements[x].Id_id == request.user.id:
            userAchievements = achievements[x]
            break

    # Add data to the context
    context = {
        'data': history,
        'profiles': profiles,
        'Achievements': userAchievements
    }

    return render(request, 'users/profile.html', context)


@login_required
def profileUpdate(request):
    """
    Pass UserUpdateForm to the webpage when requested
    You must be logged in to access the webpage if not you will be redirected to Food_Scanner-home
    :param request: The data about request made to webpage
        type - HttpRequest
    :return: The requested webpage based on the supplied template with context passed to it (Profile)
        type - HttpRequest or HttpResponseRedirect
    """

    if request.method == 'POST':
        #If a POST request method is used create a UserUpdateForm and ProfileUpdateForm
        uForm = UserUpdateForm(request.POST, instance=request.user)
        pForm = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if uForm.is_valid() and pForm.is_valid():
            # If the forms are valid save the results
            uForm.save()
            pForm.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user-profile')
    else:
        uForm = UserUpdateForm(instance=request.user)
        pForm = ProfileUpdateForm(instance=request.user.profile)

    # Add the forms to the context
    context = {
        'user_form': uForm,
        'profile_form': pForm
    }
    return render(request, 'users/profile_update.html', context)


def profile_list(request):
    """
    Checks if the user has been authenticated, taking them to the profile list page otherwise redirect them to the login page
    :param request: The pull request of the user authentication, if they are authenticated or not
        type - HttpRequest
    :return: The data request to the profiles page or redirect to the login page
        type - HttpRequest or HttpResponseRedirect
    """
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'users/profile_list.html', {'profiles': profiles})
    else:
        messages.warning(request, ("You must be logged in to view this page"))
        return redirect('auth-login')
