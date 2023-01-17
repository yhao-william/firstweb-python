from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def touhou(request,sid=0,name=""):
    return HttpResponse("TouHou.gameid:%d, game name:%s"%(sid,name))

def test404(request):
    raise Http404('?')