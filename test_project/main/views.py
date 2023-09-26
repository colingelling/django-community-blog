from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(response):
    return HttpResponse("<h1>Hello world!</h1>")


def v1(response):
    return HttpResponse("<h1>View one</h1>")
