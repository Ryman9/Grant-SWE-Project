from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.main),
    path('tickets/', views.tickets),
    path('about/', views.about),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('main/',views.main,name = "main"),
    path('login/',views.login),
    path('aboutNotLogged/', views.aboutNotLogged),
    path('homePage/',views.homePage),
    path('createTicket/',views.createTicket),
    path('updateTicket/',views.updateTicket),
    path('deleteTicket/',views.deleteTicket),

    
=======
    path('', views.home, name='home'),
    path('tickets/', views.tickets),
    path('about/', views.about),

    path('create_ticket/', views.createTicket, name='create_ticket'),
    path('update_ticket/<str:pk>', views.updateTicket, name='update_ticket'),
    path('delete_ticket/<str:pk>', views.deleteTicket, name='delete_ticket'),

    path('create_update/', views.createUpdate, name='create_update'),
    path('delete_update/<str:pk>', views.deleteUpdate, name='delete_update'),
>>>>>>> 27cb0d833d991c70c5c73656d60d42046e48e12d
]
