from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUser

def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
        else:
            messages.success(request,("Error logging in, Try again."))
            return redirect('login')
    else:
	    return render(request,'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("Logged out successfully!"))
    return redirect('main')

def register_user(request):
  if request.method =="POST":
    form = RegisterUser(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username = username, password = password)
        login(request,user)
        messages.success(request,("Congrats! Your Registration has been completed! You are now a user!"))
        return redirect('dashboard')
  else:
        form = RegisterUser()
    
  return render(request,'authenticate/register_user.html',{'form':form,})

# Create your views here.
