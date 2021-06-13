from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
#import decorators to help make sure users login before accessing some functions
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Gallery
#importing userupdate and profileupdate forms for updating our pages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, GalleryForm


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
        #g_form = GalleryForm(request.POST,request.FILES, instance=request.user.gallery)
        if u_form.is_valid() and p_form.is_valid(): #and g_form.is_valid():
            u_form.save()
            p_form.save()
            #g_form.save()
            messages.success(request, f"Your Profile Has Been Updated!")
            return redirect('profile')
        messages.error(request, f"Profile update failed")

    else:
        #galleries = Gallery.objects.all()#request.user.gallery.all()
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        #g_form = GalleryForm()
        #print(galleries)
    context = {
        'u_form': u_form,
        'p_form': p_form
        #'g_form':g_form,
        #'galleries':galleries
    }

    return render(request, 'users/profile.html', context)
'''
@login_required
def gallery(request):
    if request.method == 'POST':
        g_form = GalleryForm(request.POST,request.FILES, instance=request.user.gallery)
        if g_form.is_valid():
            g_form.save()
            messages.success(request, f"Image upload was successful")
            return redirect('profile')
        messages.error(request, f"Image upload failed")
    else:
        g_form = GalleryForm(request.user.gallery)
    context = {'g_form':g_form}
    return render(request,'users/uploads.html',context)'''
