from django.contrib import admin
from .models import User, TodoText


admin.site.register(User)
admin.site.register(TodoText)
