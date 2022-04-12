from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tickets/', views.tickets),
    path('about/', views.about),
]
