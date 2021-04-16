from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TodoText(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", null=True)
    date = models.DateField("Дата создания", default=timezone.now, blank=True, null=True)
    due = models.DateField("Дата выполнения", blank=True, null=True)
    is_done = models.BooleanField("Статус выполнения", default=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
