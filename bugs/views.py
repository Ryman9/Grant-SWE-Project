from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'bugs/dashboard.html')

def tickets(request):
    return render(request, 'bugs/tickets.html')

def about(request):
    return render(request, 'bugs/about.html')

def createTicket(request):
    form = TicketForm
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'bugs/create_form.html', context)

def updateTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticket)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'bugs/create_form.html', context)

def deleteTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == "POST":
        ticket.delete()
        return redirect('/')

    context = {'item':ticket}
    return render(request, 'bugs/delete_form.html', context)

def createUpdate(request):
    form = UpdateForm
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'bugs/create_form.html', context)

def deleteUpdate(request, pk):
    update = Update.objects.get(id=pk)
    if request.method == "POST":
        update.delete()
        return redirect('/')

    context = {'item':update}
    return render(request, 'bugs/delete_form.html', context)