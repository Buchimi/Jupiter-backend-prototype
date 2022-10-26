from operator import index
from django.urls import path
from . import views

urlpatterns = [path('', views.indexPage, name="index"),
               path('create', views.create_user),
               path("bee", views.make_bee)]
