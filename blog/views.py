from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello Word!')


def about(request):
    return HttpResponse('<h1>About</h1>')
