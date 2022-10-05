from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# return hello world


def indexPage(request):
    return HttpResponse("Hello world")
