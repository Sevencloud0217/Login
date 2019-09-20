from django.shortcuts import render
from .views import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('hello')