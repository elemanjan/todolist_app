from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)


class TodoText(models.Model):
    todo_text = models.TextField(max_length=500, null=True)
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    status = models.BooleanField(default=False)
