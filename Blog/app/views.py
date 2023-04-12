from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from .models import Blog,Comment,Profile
from .forms import CreateBlog,CommentForm,UpdateProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def Home(request):
   blog=Blog.objects.all()
   q=request.GET.get('q')
   print(q)
   if q!=None:
      print("1st block",q)
      blog=Blog.objects.filter(category=q)
   
   
   
   for i in blog:
      print(i.category)
   context={
      'blog':blog,
   }
   return render(request,'app/home.html',context)


@login_required(login_url="/login/")
def createBlog(request):
   form=CreateBlog()
   if request.method=='POST':
      form=CreateBlog(request.POST,request.FILES)
      if form.is_valid():
         form.instance.user=request.user
         form.save()
         return redirect('home')

   return render(request,'app/create.html',context={ 'form':form})      

def deleteBlog(request,id):
   Blog.objects.get(pk=id).delete()
   return redirect('myblog')

def updateBlog(request,id):
   blog=Blog.objects.get(id=id)
   form=CreateBlog(instance=blog)
   if request.method=='POST':
      form=CreateBlog(request.POST, request.FILES ,instance=blog)
      if form.is_valid:
         form.save()
         return redirect('home')
   return render(request, 'app/update.html',context={"form":form})      
      

def loginBlog(request):
   print("sada")
   if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      print("check")
      user=authenticate(request,username=username,password=password)

      if user is not None:
         login(request, user)
         return redirect('home')
      else:
         messages.error(request, 'Invalid Credentials')

   return render(request,'app/login.html')
   


def registerBlog(request):
  if request.method=='POST':
   uname=request.POST.get('username')
   email=request.POST.get('email')
   pass1=request.POST.get('password1')
   pass2=request.POST.get('password2')
   state=request.POST.get('state')
   print(uname,email,pass1,pass2)
   new_user=User.objects.create_user(uname,email,pass1)
   new_profile=Profile.objects.create(name='Untitled',email=email,state=state)
   new_user.save()
   return redirect('login')

  return render(request,'app/register.html')


@login_required(login_url="/login/")
def profile(request):
   fprofile=UpdateProfile(instance=request.user.profile)
   if request.method=='POST':
      data=request.POST or None
      media=request.FILES or None
      fprofile=UpdateProfile(data,media,instance=request.user.profile)
      if fprofile.is_valid():
         fprofile.save()
         return redirect('profile')
   context={
      'fprofile':fprofile
   }
   return render(request,'app/profile.html',context)



def blogDetail(request,id):
   
   blog=Blog.objects.get(pk=id)
   print("Hello")
   context={
      'blog':blog
   }
   return render(request,'app/detail.html',context)




def myBlog(request):
   myblog=Blog.objects.filter(user=request.user)
   context={
      'myblog':myblog
   }
   return render(request,'app/myblog.html',context)






def logout_view(request):
   logout(request)
   return redirect('home')
