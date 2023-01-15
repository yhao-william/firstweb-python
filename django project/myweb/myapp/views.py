from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Stu
from myapp.models import TouHou

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def add(request):
    lists = Stu.objects.all()
    for stu in lists:
        print(Stu)
    print(Stu.objects.get(id=3))
    return HttpResponse("Add.....")

def TouHou(request):
    lists = TouHou.objects.all()
    for touhou in lists:
        print(TouHou)
    print(TouHou.objects.get(id=3))
    return HttpResponse("欢迎来到人间之里。")