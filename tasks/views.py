from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from tasks.models import Tasks
from tasks.forms import TaskForm


class TasksListView(ListView):
    model = Tasks
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = '/tasks/'
    success_message = 'Задача успешно создана'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = '/tasks/'
    success_message = 'Задача успешно изменена'


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = '/tasks/'
    template_name = 'tasks/task_delete.html'
    success_message = 'Задача успешно удалена'


class TaskDetailsView(DetailView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'tasks/task_details.html'
