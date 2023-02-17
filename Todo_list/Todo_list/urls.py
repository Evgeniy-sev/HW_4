from django.contrib import admin
from django.urls import path, include
from tasks import views
from tasks.views import (
    TasksListView,
    TasksCreateView,
    TasksDeleteView,
    TaskUpdateView,
    TasksCompleteListView,
    TasksViewSet,
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TasksViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("uncompleted_tasks/", TasksListView.as_view(), name="tasksList"),
    path("add_tasks/", TasksCreateView.as_view()),
    path("delete_tasks/<int:pk>", TasksDeleteView.as_view(), name="delete"),
    path("update_tasks/<int:pk>", TaskUpdateView.as_view(), name="update"),
    path("completed_tasks/", TasksCompleteListView.as_view()),
    path('api/', include(router.urls)),
]

