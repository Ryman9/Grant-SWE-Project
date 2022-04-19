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
    path('deleteTicket/', views.deleteTicketPage),
    path('tickets/', views.ticketsPage),
    path('ticket/details/<str:id>', views.ticketDetailsPage),
    path('profile/<str:id>', views.profilePage),
    # backend
    path('submit_ticket/', views.submit_ticket),
    path('login_user/', views.login_user),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('ticket/update/<str:id>', views.update_ticket),
    path('ticket/delete/<str:id>', views.delete_ticket),
    path('search_tickets/', views.search_tickets),
    path('search_categories/', views.search_categories1),
    path('search_categories/<str:q>', views.search_categories2),
]
