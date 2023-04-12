from .models import Blog,Profile,Comment
from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateBlog(ModelForm):
   
   class Meta:
      model=Blog
      fields=['title','description','category','bimage']

      widgets ={
         'title': forms.TextInput(attrs={'class': 'form-control'}),
         'description': forms.Textarea(attrs={'class': 'form-control'}),
         'category': forms.Select(attrs={'class': 'form-control'}),
      }

class UpdateProfile(ModelForm):
   class Meta:
      model=Profile
      fields=['user','name','email','state','image']

      widgets ={
         'user': forms.TextInput(attrs={'class': 'form-control'}),
         'name': forms.TextInput(attrs={'class': 'form-control'}),
         'email': forms.TextInput(attrs={'class': 'form-control'}),
         'state': forms.TextInput(attrs={'class': 'form-control'}),
      }
class CommentForm(ModelForm):
   class Meta:
      model=Comment
      fields=['body']
