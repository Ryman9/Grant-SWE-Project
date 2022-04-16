from django.urls import path
from . import views

urlpatterns = [

    path('', views.main),
    path('tickets/', views.tickets),
    path('about/', views.about),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('main/',views.main,name = "main"),
    path('login/',views.login),
    path('aboutNotLogged/', views.aboutNotLogged),
    path('homePage/',views.homePage, name ="homePage"),
    path('createTicket/',views.createTicket),
    path('updateTicket/',views.updateTicket),
    path('deleteTicket/',views.deleteTicket),
    path('', views.home, name='home'),
    path('tickets/', views.tickets),
    path('about/', views.about),
    path('login_user', views.login_user, name = "login"),
    path('logout_user',views.logout_user, name = 'logout'),
    path('register_user',views.register_user, name ='register_user')

]
