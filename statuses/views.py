from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from statuses.models import Statuses
from statuses.forms import StatusForm


class StatusesListView(ListView):
    model = Statuses
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'


class StatusCreateView(CreateView):
    model = Statuses
    form_class = StatusForm
    template_name = 'statuses/status_create.html'
    success_url = '/statuses/'


class StatusUpdateView(SuccessMessageMixin, UpdateView):
    model = Statuses
    form_class = StatusForm
    template_name = 'statuses/status_create.html'
    success_url = '/statuses/'
    success_message = 'Статус успешно изменён'


class StatusDeleteView(SuccessMessageMixin, DeleteView):
    model = Statuses
    context_object_name = 'status'
    success_url = '/statuses/'
    template_name = 'statuses/status_delete.html'
    success_message = 'Статус успешно удалён'
