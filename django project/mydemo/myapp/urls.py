from django.urls import path,re_path
from . import views

urlpatterns = [
    path("index/",views.index),
    path("test404/",views.test404),
    path("touhou/<int:sid>",views.touhou),
    path("touhou/<int:sid>/<str:name>",views.touhou),
]