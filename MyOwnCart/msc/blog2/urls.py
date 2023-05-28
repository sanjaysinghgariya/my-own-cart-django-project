from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('postblog/', views.postblog),
    path('showblog/', views.showblog),
    path('showingblog/<int:my_id>', views.showingblog),
    path('error/', views.error_handling)
]