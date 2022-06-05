from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm): 
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

class UpdateUserForm(forms.ModelForm):
  email= forms.EmailField(max_length=150)

  class Meta:
    model = User
    fields = ('username', 'email')

class UpdateUserProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('name','profile_picture','bio')