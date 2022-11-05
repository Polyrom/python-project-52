from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import LoginRequiredMessageMixin, UserMatchesAuthorMixin
from django_filters.views import FilterView
from tasks.forms import TaskFilter
from tasks.models import Task
from tasks.forms import TaskForm
from django.utils.translation import gettext as _


class TasksListView(LoginRequiredMessageMixin, FilterView):
    filterset_class = TaskFilter
    template_name = 'tasks/tasks_list.html'
    redirect_field_name = ''


class TaskCreateView(LoginRequiredMessageMixin,
                     SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = '/tasks/'
    success_message = _('Task created successfully')
    redirect_field_name = ''

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMessageMixin,
                     SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = '/tasks/'
    success_message = _('Task updated successfully')
    redirect_field_name = ''


class TaskDeleteView(LoginRequiredMessageMixin, UserMatchesAuthorMixin,
                     SuccessMessageMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = '/tasks/'
    template_name = 'tasks/task_delete.html'
    success_message = _('Task deleted successfully')
    redirect_field_name = ''


class TaskDetailsView(LoginRequiredMessageMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_details.html'
    redirect_field_name = ''
