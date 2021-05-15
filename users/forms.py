from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#importing the profile model so user can change profile pic
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#user can change username amd email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#changing dp
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

#we'll update these two new forms in our vie