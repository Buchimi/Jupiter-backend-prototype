from typing import ValuesView
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from clubs.models import Club
# Create your views here.


def index(request):
    # get a list of clubs
    data = Club.objects.all()[:20]
    return JsonResponse(data, safe=False)
    # we can also do queries here
    pass


# club/id
def get_club(request: HttpRequest, value):
    # we want to get the club that maps to this url
    club = Club.objects.get(id=value)
    return JsonResponse(club)
    pass

#club/post
def create_club(request : HttpRequest):
    data = request.POST
    pass