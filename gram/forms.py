from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

class SignUpForm(UserCreationForm): 
	email = forms.EmailField(max_length=150,required=True)

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

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('image', 'caption')

class CommentForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['comment'].widget = forms.TextInput()
    self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'


