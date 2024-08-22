from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

# 实现HTML页面表达的内容


def hello_world(request):
    return HttpResponse("hello worlddededede")


def hello_world1(request):
    return HttpResponse("helloxxx")
