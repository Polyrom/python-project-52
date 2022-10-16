from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from tasks.models import Task
from tasks.forms import TaskForm


class TasksListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = '/tasks/'
    success_message = 'Задача успешно создана'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = '/tasks/'
    success_message = 'Задача успешно изменена'


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = '/tasks/'
    template_name = 'tasks/task_delete.html'
    success_message = 'Задача успешно удалена'

    def dispatch(self, request, *args, **kwargs):
        if not request.user == self.model.objects.get(id=kwargs['pk']).author:
            messages.add_message(request, messages.ERROR,
                                 'Задачу может удалить только её автор')
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class TaskDetailsView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_details.html'
