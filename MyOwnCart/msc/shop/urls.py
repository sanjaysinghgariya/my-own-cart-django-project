from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("search/ ", views.search, name="search"),
    path("about/", views.about),
    path("contact/", views.contact),
    path("tracker/", views.tracker),
    path("search/", views.search),
    path("products/<int:my_id>", views.prodView),
    path("checkout/", views.checkout),
    path("returns_orders", views.returns_orders),
    path("grocery", views.grocery),
    path("product_info", views.product),
    path('basic', views.Basic),
    path("test", views.onlyfortesting)

]