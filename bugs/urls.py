from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tickets/', views.tickets),
    path('about/', views.about),

    path('create_ticket/', views.createTicket, name='create_ticket'),
    path('update_ticket/<str:pk>', views.updateTicket, name='update_ticket'),
    path('delete_ticket/<str:pk>', views.deleteTicket, name='delete_ticket'),

    path('create_update/', views.createUpdate, name='create_update'),
    path('delete_update/<str:pk>', views.deleteUpdate, name='delete_update'),
]
