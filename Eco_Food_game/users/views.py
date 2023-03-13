from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import History

# Create your views here.

def register(request):
    """
    Pass User registration form to the register webpage based on the register.html template
    param - request:
        type - HttpRequest object
        contents -  Data about request made to webpage
    return - Rendered webpage
        Returns the requested webpage based on the supplied template with context passed to it 
    """
    #If the method of request is POST
    if request.method == 'POST':
        #Create a form using the UserRegistrationForm method from users/forms.py
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #If the form is valid, Save it then redirect to the login page
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You can now log in!')
            return redirect('auth-login')
    else:
        form = UserRegisterForm()

    #Return and render the webpage and pass the form into the template
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """
    Pass the profile information to the correct webpage
    You need to be logged in to access webpage otherwise you will be redirected to Food_Scanner-home 
    param - request:
        type - HttpRequest object
        contents -  Data about request made to webpage
    return - Rendered webpage
        Returns the requested webpage based on the supplied template with context passed to it 
    """
    
    #Collects history from database
    history = History.objects.order_by('date_Added')

    #Add data to the context
    context = {
        'data': history
    }

    return render(request, 'users/profile.html', context)


@login_required
def profileUpdate(request):
    """
    Pass UserUpdateForm to the webpage when requested
    You must be logged in to access the webpage if not you will be redirected to Food_Scanner-home
    param - request:
        type - HttpRequest object
        contents -  Data about request made to webpage
    return - Rendered webpage
        Returns the requested webpage based on the supplied template with context passed to it 
    """

    if request.method == 'POST':
        #If a POST request method is used create a UserUpdateForm and ProfileUpdateForm
        uForm = UserUpdateForm(request.POST, instance=request.user)
        pForm = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if uForm.is_valid() and pForm.is_valid():
            #If the forms are valid save the results
            uForm.save()
            pForm.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user-profile')
    else:
        uForm = UserUpdateForm(instance=request.user)
        pForm = ProfileUpdateForm(instance=request.user.profile)

    #Add the forms to the context
    context = {
        'user_form': uForm,
        'profile_form': pForm
    }
    return render(request, 'users/profile_update.html', context)
