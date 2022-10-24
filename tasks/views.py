from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from tasks.forms import TaskFilter
from django.contrib import messages
from tasks.models import Task
from tasks.forms import TaskForm
from django.shortcuts import redirect
from task_manager.mixins import NotLoggedInMessageMixin


class TasksListView(NotLoggedInMessageMixin, LoginRequiredMixin, FilterView):
    filterset_class = TaskFilter
    template_name = 'tasks/tasks_list.html'


class TaskCreateView(NotLoggedInMessageMixin, LoginRequiredMixin,
                     SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = '/tasks/'
    success_message = 'Задача успешно создана'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(NotLoggedInMessageMixin, LoginRequiredMixin,
                     SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = '/tasks/'
    success_message = 'Задача успешно изменена'


class TaskDeleteView(NotLoggedInMessageMixin, LoginRequiredMixin,
                     SuccessMessageMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = '/tasks/'
    template_name = 'tasks/task_delete.html'
    success_message = 'Задача успешно удалена'

    def dispatch(self, request, *args, **kwargs):
        if not request.user == self.model.objects.get(id=kwargs['pk']).author:
            messages.add_message(
                request, messages.ERROR,
                'Задачу может удалить только её автор'
            )
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class TaskDetailsView(NotLoggedInMessageMixin, LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_details.html'
