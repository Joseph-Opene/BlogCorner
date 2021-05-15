from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
#import decorators to help make sure users login before accessing some functions
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#importing userupdate and profileupdate forms for updating our pages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

#making an account creation form. Creating a new user
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your Account Has Been Created You're Now Able To Log In")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

#we create a users profile
#then we add @ as a decorater that adds more funtions to an existing function, the @login_required tells the code that before it goes anywhere u need to log in first
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your Profile Has Been Updated!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)