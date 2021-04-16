from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo),
    path('todo_delete/<int:todo_id>/', views.todo_delete),
    path('todo_update/<int:todo_id>/', views.todo_update),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('done/<int:pk>/', views.done),
]
