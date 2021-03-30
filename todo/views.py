import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, TodoText


def todo(request):
    user_list = User.objects.all()
    template = loader.get_template('index.html')
    context = {
        'users': user_list,
    }
    return HttpResponse(template.render(context, request))


