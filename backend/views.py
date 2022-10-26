from crypt import methods
import imp
import re
from telnetlib import STATUS
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from .forms import Bee
from .forms import UserForm
# Create your views here.

# return hello world


def indexPage(request):
    return HttpResponse("Hello world")


@csrf_exempt
def create_user(request: HttpRequest):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # we want to add the form to the database
            # form.save()
            print(request.body)

    return redirect("http://127.0.0.1:5500/form.html")


@csrf_exempt
def make_bee(request: HttpRequest):
    print(request)
    if request.method == "POST":
        form = Bee(request.POST)
        if form.is_valid():
            print(form)
            form.save()
    return HttpResponse("")
