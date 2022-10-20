from tasks.views import TasksListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailsView
from django.urls import path


urlpatterns = [
    path('', TasksListView.as_view(), name='tasks.list'),
    path('<int:pk>/', TaskDetailsView.as_view(), name='task.details'),
    path('create/', TaskCreateView.as_view(), name='task.create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task.update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task.delete'),
]
