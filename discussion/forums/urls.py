from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('home', views.home,name = "forum"),
    path('forum',views.forum,name = "akforum"),
    path('sign_up/',views.sign_up,name="sign-up")
]