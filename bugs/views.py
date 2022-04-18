from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

# Andrew
def homePage(request):
    context = {"updates": Update.objects.all()}
    context["logged_in"] = request.user.is_authenticated
    if request.user.is_authenticated:
        context["totalTickets"] = len(searchTickets(request))
        context["createTickets"] = searchTickets(request, createUser=request.user.username)
        context["assignTickets"] = searchTickets(request, assignUser=request.user.username)
        return render(request, 'bugs/dashboard.html', context)
    else:
        return render(request, 'bugs/landing.html')

#Antonio: defines the views and provides user login authenication for the system
@login_required(login_url="/login")
def dashboardPage(request):
    return homePage(request)

@login_required(login_url="/login")
def ticketsPage(request):
    return render(request, 'bugs/tickets.html')

def aboutPage(request):
    return render(request, 'bugs/about.html')

# LOGIN
def loginPage(request):
    return render(request, 'bugs/login.html', context={"form": LoginUserForm()})

def registerPage(request):
    return render(request, 'authenticate/register.html', context={"form": RegisterUserForm()})

# TICKETS
@login_required(login_url="/login")
def createTicketPage(request):
    return render(request,'bugs/create_form.html', context={"form": TicketForm()})

@login_required(login_url="/login")
def updateTicketPage(request):
    return render(request,'bugs/update_form.html')

@login_required(login_url="/login")
def deleteTicketPage(request):
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

# USERS
def login_user(request):
   if request.method == "GET":
        form = LoginUserForm(request.GET)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.success(request, ("Error logging in. Try again."))
                return redirect('login')
        else:
            messages.success(request, ("Error logging in. Try again."))
            return redirect('login')
   else:
	    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("Logged out."))
    return redirect('home')

def register_user(request):
  if request.method == "GET":
    form = RegisterUserForm(request.GET)
    if form.is_valid():
        firstName = form.cleaned_data["first_name"]
        lastName = form.cleaned_data["last_name"]
        position = form.cleaned_data["position"]
        department = form.cleaned_data["department"]
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        employee = Employee.objects.create(firstName=firstName, lastName=lastName, username=username, position=position, department=department)
        employee.save()

        form.save()

        user = authenticate(username=username, password=password)
        login(request, user)

        messages.success(request, ("Your registration is complete!"))
        return redirect('dashboard')
  else:
        form = RegisterUser()
  return render(request,'authenticate/register.html',{'form':form})

# TICKETS
def searchTickets(request, id=-1, category="", urgency="", createDate="", createUser="", assignUser=""):
    res = Ticket.objects.all()
    if id > -1:
        res = res.filter(ticketId__exact=id)
    if len(category) > 0:
        res = res.filter(category__exact=category)
    if len(urgency) > 0:
        res = res.filter(urgency__exact=urgency)
    if len(createDate) > 0:
        res = res.filter(timestamp__exact=createDate)

    if len(createUser) > 0:
        createUsernames = Employee.objects.filter(username__exact=createUser)
        createUser1 = -1
        if len(createUsernames) > 0:
            createUser1 = createUsernames[0].userId
        if createUser1 > -1:
            res = res.filter(createdBy_id__exact=createUser1)

    if len(assignUser) > 0:
        assignUsernames = Employee.objects.filter(username__exact=assignUser)
        if len(assignUsernames) > 0:
            assignUser1 = assignUsernames[0].userId
        assignUser1 = -1
        if assignUser1 > -1:
            res = res.filter(Q(assignedTo_id__exact=assignUser1))

    return res

def submitTicket(request):
    if request.method == "GET":
        # form = CreateTicketForm(request.GET)
        form = TicketForm(request.GET)
        if form.is_valid():
            form.save()
            # title = form.cleaned_data['title']
            # category = form.cleaned_data['category']
            # urgency = form.cleaned_data['urgency']
            messages.success(request, ("Ticket submitted"))
    return redirect('dashboard')

def ticketPage(request, id):
    id1 = int(id)
    context = {"ticket": searchTickets(request, id=id1)[0]}
    return render(request,'bugs/ticket_details.html',context)

def ticket_delete(request, id):
    id1 = int(id)
    t = searchTickets(request, id=id1)[0]
    t.delete()
    return redirect('dashboard')
