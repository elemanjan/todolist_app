from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class TodoText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_text = models.TextField(max_length=500, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo_text


