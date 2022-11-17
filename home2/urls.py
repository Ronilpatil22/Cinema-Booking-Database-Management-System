import os
from django.contrib import admin
from django.urls import path,include
from home2 import views

urlpatterns = [
    path('', views.home,name="home"),
    path('index.html',views.home,name="home"),
    path('index',views.home,name="home"),
    path('home',views.home,name="home"),
    path('movies.html',views.movies,name="movies"),
    path('movies',views.movies,name="movies"),
    path('login', views.handleLogin,name="handleLogin"), 
    path('login.html', views.handleLogin,name="handleLogin"), 
    path('sign_in.html', views.handleLogin,name="handleLogin"), 
    path('logout', views.handleLogout,name="handleLogout"),
    path('signup', views.handleSignup,name="handleSignup"),
    path('Contact_Us.html', views.contact_us,name="Contact_Us"),
    path('contact_us', views.contact_us,name="Contact_Us"),
    path('about.html', views.about,name="about"),
    path('about', views.about,name="about"),
    path('ticket-booking.html', views.book,name="book"),
    path('seat_sel.html', views.seat,name="seat"),
    path('seat', views.seat,name="seat"),
    path('book', views.book,name="book"),
    
    
]