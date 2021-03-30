import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, TodoText


def home(request):
    return render(request, 'todo/index.html')


