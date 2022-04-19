from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

def valuesListToList(vl):
    return [item for t in vl for item in t]

# Andrew
def homePage(request):
    context = {"updates": Update.objects.all()}
    context["logged_in"] = request.user.is_authenticated
    if request.user.is_authenticated:
        context["totalTicketsCount"] = Ticket.objects.all().filter(Q(status='Created') | Q(status='In Progress')).count()
        context["pendingTicketsCount"] = Ticket.objects.all().filter(status='Created').count()
        context["inprogressTicketsCount"] = Ticket.objects.all().filter(status='In Progress').count()
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
    context = {"tickets": searchTickets(request)}
    context["totalTicketsCount"] = Ticket.objects.all().filter(Q(status='Created') | Q(status='In Progress')).count()
    context["pendingTicketsCount"] = Ticket.objects.all().filter(status='Created').count()
    context["inprogressTicketsCount"] = Ticket.objects.all().filter(status='In Progress').count()
    context["createTickets"] = searchTickets(request, createUser=request.user.username)
    context["query"] = request.GET
    return render(request, 'bugs/tickets.html', context)

def aboutPage(request):
    return render(request, 'bugs/about.html')

def ticketDetailsPage(request, id):
    id1 = int(id)
    context = {"ticket": searchTickets(request, id=id1)[0]}
    context["users"] = valuesListToList(Employee.objects.values_list("username"))
    return render(request,'bugs/ticket_details.html',context)

def updateDetailsPage(request, id):
    id1 = int(id)
    context = {"update": Update.objects.filter(updateId__exact=id1)[0]}
    context["ticket"] = context["update"]
    context["users"] = valuesListToList(Employee.objects.values_list("username"))
    return render(request,'bugs/update_details.html',context)

# LOGIN
def loginPage(request):
    return render(request, 'bugs/login.html', context={"form": LoginUserForm()})

def registerPage(request):
    return render(request, 'authenticate/register.html', context={"form": RegisterUserForm()})

@login_required(login_url="/login")
def profilePage(request, id):
    res = Employee.objects.all().filter(username=id)[0]
    res.is_authenticated = True
    return render(request, 'bugs/profile.html', {'user': res})

# TICKETS
@login_required(login_url="/login")
def createTicketPage(request):
    return render(request,'bugs/create_ticket.html', context={"form": TicketForm()})

@login_required(login_url="/login")
def updateTicketPage(request):
    return render(request,'bugs/update_ticket.html')

@login_required(login_url="/login")
def deleteTicketPage(request):
    return render(request,'bugs/delete_ticket.html')

# UPDATES
@login_required(login_url="/login")
def createUpdatePage(request):
    return render(request,'bugs/create_update.html', context={"form": UpdateForm()})

def submit_update(request):
    if request.method == "GET":
        form = UpdateForm(request.GET)
        if form.is_valid():
            form.save()
            # title = form.cleaned_data['title']
            # category = form.cleaned_data['category']
            # urgency = form.cleaned_data['urgency']
            messages.success(request, ("Update submitted"))
    return redirect('dashboard')

def delete_update(request, id):
    id1 = int(id)
    t = Update.objects.filter(id=id1)[0]
    if t is not None:
        t.delete()
    return redirect('dashboard')

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
def searchTickets(request, id=-1, title="", category="", urgency="", createDate="", createUser="", assignUser=""):
    res = Ticket.objects.all()
    if id > -1:
        res = res.filter(ticketId__exact=id)
    if len(title) > 0:
        res = res.filter(title__icontains=title)
    if len(category) > 0:
        res = res.filter(category__iexact=category)
    if len(urgency) > 0:
        res = res.filter(urgency__iexact=urgency)
    if len(createDate) > 0:
        res = res.filter(timestamp__iexact=createDate)
    if len(createUser) > 0:
        createUsernames = Employee.objects.filter(username__exact=createUser)
        createUser1 = -1
        if len(createUsernames) > 0:
            createUser1 = createUsernames[0].userId
        if createUser1 > -1:
            res = res.filter(createdBy_id__exact=createUser1)
    if len(assignUser) > 0:
        assignUsernames = Employee.objects.filter(username__exact=assignUser)
        assignUser1 = -1
        if len(assignUsernames) > 0:
            assignUser1 = assignUsernames[0].userId
        if assignUser1 > -1:
            res = res.filter(assignedTo_id__exact=assignUser1)
    return res

def update_ticket(request, id):
    if request.method == "GET":
        t = Ticket.objects.filter(ticketId__exact=id)[0]
        t.title = request.GET["title"]
        t.description = request.GET["description"]
        t.status = request.GET["status"]
        t.urgency = request.GET["urgency"]
        t.assignedTo = Employee.objects.filter(username__exact=request.GET["assignedTo"])[0]
        t.save()
        messages.success(request, ("Ticket updated"))
    return redirect('tickets')

def submit_ticket(request):
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

def delete_ticket(request, id):
    id1 = int(id)
    t = searchTickets(request, id=id1)[0]
    if t is not None:
        t.delete()
    return redirect('tickets')

def search_tickets(request):
    if request.method == "GET":
        id = int(request.GET["id"]) if len(request.GET["id"]) > 0 else -1
        title = request.GET["title"]
        context = {"tickets": searchTickets(request, id=id, title=title)}
        context["totalTicketsCount"] = Ticket.objects.all().filter(Q(status='Created') | Q(status='In Progress')).count()
        context["pendingTicketsCount"] = Ticket.objects.all().filter(status='Created').count()
        context["inprogressTicketsCount"] = Ticket.objects.all().filter(status='In Progress').count()
        context["createTickets"] = searchTickets(request, createUser=request.user.username)
        context["query"] = request.GET
        return render(request,'bugs/tickets.html',context)
    return render(request,'bugs/tickets.html')

def search_categories1(request):
    return HttpResponse()

def search_categories2(request, q):
    txt = ""
    if request.method == "GET":
        lt = Ticket.objects.values_list("category")
        l = valuesListToList(lt)
        if len(q) > 0:
            for i in l:
                if q.lower() not in i.lower():
                    l.remove(i)
        s = set(l)
        txt = str(s)
        txt = txt[1:-1].replace("'", "")
    return HttpResponse(txt)
