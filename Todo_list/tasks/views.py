from django.shortcuts import render
from tasks.models import Tasks
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    View,
    DeleteView,
    UpdateView,
)
from rest_framework import generics
from .serializers import TasksSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FilterSet


def index(request):
    return render(request, "index.html")


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilterSet


class TasksListView(ListView):  # список незавершенных задач
    model = Tasks
    context_object_name = "tasks_"
    queryset = Tasks.objects.filter(is_active=True)
    template_name = "uncompleted.html"


class TasksCompleteListView(ListView):  # список завершенных задач
    model = Tasks
    context_object_name = "tasks_compl_"
    queryset = Tasks.objects.filter(is_active=False)
    template_name = "completed.html"


class TasksCreateView(CreateView):  # создание новой задачи
    model = Tasks
    fields = ["title"]
    template_name = "task_create.html"
    success_url = "/"


class TaskUpdateView(UpdateView):  # редактирование задачи
    model = Tasks
    template_name = "task_update.html"
    fields = ["title", "is_active"]
    success_url = "/"


class TasksDeleteView(DeleteView):  # удаление задачи
    model = Tasks
    template_name = "task_delete.html"
    success_url = "/"
