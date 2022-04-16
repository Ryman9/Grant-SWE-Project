from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUser

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

#Antonio: defines the views and provides user login authenication for the system
def main(request):
    return render(request, 'bugs/main.html')

@login_required(login_url="/users/login_user")
def dashboard(request):
    return render(request, 'bugs/dashboard.html')

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

# Create your views here.
def home(request):
    context = {"updates": Update.objects.all()}
    context["logged_in"] = request.user.is_authenticated
    if request.user.is_authenticated:
        context["tickets"] = searchTickets(assignUser=0)
    return render(request, 'bugs/dashboard.html', context)


@login_required(login_url="/users/login_user")
def tickets(request):
    return render(request, 'bugs/tickets.html')

@login_required(login_url="/users/login_user")
def about(request):
    return render(request, 'bugs/about.html')


def login(request):
    return render(request, 'bugs/login.html')

def aboutNotLogged(request):
    return render(request, 'bugs/aboutNotLogged.html')

def homePage(request):
    return render(request, 'bugs/homePage.html')

@login_required(login_url="/users/login_user")
def createTicket(request):
    return render(request,'bugs/create_form.html')

@login_required(login_url="/users/login_user")
def updateTicket(request):
    return render(request,'bugs/update_form.html')

@login_required(login_url="/users/login_user")
def deleteTicket(request):
    return render(request,'bugs/delete_form.html')

#Antonio - commented out due to merge of two different code bases
#@csrf_exempt
#def createTicket(request):
    #form = TicketForm
   # if request.method == 'POST':
    #    form = TicketForm(request.POST)
     #   if form.is_valid():
      #      form.save()
       #     return redirect('/')

   # context = {'form':form}
    #return render(request, 'bugs/create_form.html', context)

@csrf_exempt
#def updateTicket(request, pk):
 #   ticket = Ticket.objects.get(id=pk)
  #  form = TicketForm(instance=ticket)

   # if request.method == 'POST':
    #    form = TicketForm(request.POST, instance=ticket)
     #   if form.is_valid():
      #      form.save()
       #     return redirect('/')

  #  context = {'form':form}
   # return render(request, 'bugs/create_form.html', context)

#@csrf_exempt
#def deleteTicket(request, pk):
 #   ticket = Ticket.objects.get(id=pk)
  #  if request.method == "DELETE":
   #     ticket.delete()
    #    return redirect('/')

    #context = {'item':ticket}
    #return render(request, 'bugs/delete_form.html', context)

#@csrf_exempt
#def createUpdate(request):
 #   form = UpdateForm
  #  if request.method == "POST":
   #     form = UpdateForm(request.POST)
   #     if form.is_valid():
    #        form.save()
    #        return redirect('/')

   # context = {'form':form}
    #return render(request, 'bugs/create_form.html', context)

#@csrf_exempt
#def deleteUpdate(request, pk):
 #   update = Update.objects.get(id=pk)
 #   if request.method == "DELETE":
  #      update.delete()
   #     return redirect('/')

    #context = {'item':update}
    #return render(request, 'bugs/delete_form.html', context)

# Andrew
def searchTickets(category="", urgency="", createDate="", createUser=-1, assignUser=-1):
    res = Ticket.objects.all()
    if len(category) > 0:
        res = res.filter(Q(category__equals=category))
    if len(urgency) > 0:
        res = res.filter(Q(urgency__equals=urgency))
    if len(createDate) > 0:
        res = res.filter(Q(timestamp__equals=createDate))
    if createUser > 0:
        res = res.filter(Q(createdBy_id__equals=createUser))
    if assignUser > 0:
        res = res.filter(Q(assignedTo_id__equals=assignUser))
    return res

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
        return redirect('homePage')
  else:
        form = RegisterUser()
    
  return render(request,'authenticate/register_user.html',{'form':form,})

# Create your views here.
# Login code
# @csrf_exempt
# def handle_login(request):
# 	if not request.user.is_authenticated:
# 		email = request.POST["email"]
# 		key = request.POST["key"]
# 		user = authenticate(request, username=email, password=key)
#
# 		if user is not None and key == _key:
# 			login(request, user)
# 			if request.user.is_authenticated:
# 				request.session.set_expiry(1800) # 30 min.
# 				return redirect("?")
# 			else:
# 				return render(request, "error.html")
# 		else:
# 			return render(request, "error.html")
# 	else:
# 		return redirect("?")
#
# @login_required(login_url="?")
# @login_required

