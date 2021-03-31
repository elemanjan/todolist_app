import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, TodoText
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect


def home(request):
    todo_items = TodoText.objects.all().order_by('-date')
    return render(request, 'todo/index.html', {
        'todo_items': todo_items
    })


@csrf_exempt
def add_todo(request):
    add_date = timezone.now().strftime('%Y-%m-%dT%H:%M:%S')
    todo_text = request.POST['todo_text']
    print(add_date)
    print(todo_text)
    length_todos = TodoText.objects.all().count()
    TodoText.objects.create(date=add_date, todo_text=todo_text)
    return HttpResponseRedirect('/')


@csrf_exempt
def todo_delete(request, todo_id):
    TodoText.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
