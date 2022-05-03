from django.urls import path, include
# from django.conf.urls import url
from .views import (TodoListApiView, TodoDetailApiView)

urlpatterns = [
    path('', TodoListApiView.as_view()),
    path('<int:todo_id>/', TodoDetailApiView.as_view())

]
