from django.urls import path
from tasks.views import TasksListView, TaskCreateView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('', TasksListView.as_view(), name='tasks.list'),
    path('create/', TaskCreateView.as_view(), name='task.create'),
    path('<int:pk>/update', TaskUpdateView.as_view(), name='task.update'),
    path('<int:pk>/delete', TaskDeleteView.as_view(), name='task.delete'),
]