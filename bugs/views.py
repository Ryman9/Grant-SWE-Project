from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'bugs/dashboard.html')

def tickets(request):
    return render(request, 'bugs/tickets.html')

def about(request):
    return render(request, 'bugs/about.html')