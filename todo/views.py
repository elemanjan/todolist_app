import requests
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .form import RegisterForm
from .models import TodoText
from django.utils import timezone
from django.http import HttpResponseRedirect


def home(request):
    todo_items = TodoText.objects.all().order_by('due')
    current_user = request.user.id
    todo_items = TodoText.objects.filter(user_id=current_user)
    return render(request, 'todo/todolist.html', {
        'todo_items': todo_items
    })


def add_todo(request):
    add_date = timezone.now().strftime("%Y-%m-%d")
    title = request.POST['todo_title']
    due = request.POST['due_on']
    current_user = request.user.id
    TodoText.objects.create(date=add_date, title=title, due=due, user_id=current_user)
    return HttpResponseRedirect('/')


def todo_delete(request, todo_id):
    TodoText.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')


def todo_update(request, todo_id):
    task = TodoText.objects.get(id=todo_id)
    task.title = request.POST['todo_title']
    task.description = request.POST['todo_desc']
    task.due = request.POST['due_on']
    task.save()
    return HttpResponseRedirect('/')


def signup(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        auth_login(request, user)
        return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'todo/signup.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("todo:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="todo/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("todo:home")


def done(request, pk):
    task = TodoText.objects.get(id=pk)
    task.is_done = True
    task.save()
    return HttpResponseRedirect('/')

