from django.urls import path
from . import views

urlpatterns = [
    # pages
    path('', views.homePage, name="home"),
    path('about/', views.aboutPage, name="about"),
    path('tickets/', views.ticketsPage, name="tickets"),
    path('dashboard/', views.dashboardPage, name="dashboard"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('createTicket/', views.createTicketPage),
    path('updateTicket/', views.updateTicketPage),
    path('deleteTicket/', views.deleteTicketPage),
    path('tickets/', views.ticketsPage),
    path('ticket/details/<str:id>', views.ticketDetailsPage),
    # backend
    path('submit_ticket/', views.submit_ticket),
    path('login_user/', views.login_user),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('ticket/delete/<str:id>', views.ticket_delete),
    path('search_tickets/', views.search_tickets),
]
