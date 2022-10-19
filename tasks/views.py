from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView
from tasks.forms import TaskFilter
from django.contrib import messages
from tasks.models import Task
from tasks.forms import TaskForm
from django.shortcuts import redirect
from task_manager import settings


class TasksListView(FilterView):
    filterset_class = TaskFilter
    template_name = 'tasks/tasks_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = '/tasks/'
    success_message = 'Задача успешно создана'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = '/tasks/'
    success_message = 'Задача успешно изменена'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = '/tasks/'
    template_name = 'tasks/task_delete.html'
    success_message = 'Задача успешно удалена'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect(settings.LOGIN_URL)
        if not request.user == self.model.objects.get(id=kwargs['pk']).author:
            messages.add_message(request, messages.ERROR,
                                 'Задачу может удалить только её автор')
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class TaskDetailsView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_details.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)
