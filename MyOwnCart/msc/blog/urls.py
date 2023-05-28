from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("blogpost/", views.blogpost),
    path("makeblog/", views.makeblog),
    path("showblog/", views.showblog),

]