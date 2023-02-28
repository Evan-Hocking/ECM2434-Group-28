from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You can now log in!')
            return redirect('auth-login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        uForm = UserUpdateForm(request.POST, instance=request.user)
        pForm = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user-profile')
    else:
        uForm = UserUpdateForm(instance=request.user)
        pForm = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': uForm,
        'profile_form': pForm
    }
    return render(request, 'users/profile.html', context)
