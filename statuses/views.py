from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.db.models.deletion import ProtectedError
from django.contrib import messages
from statuses.models import Status
from statuses.forms import StatusForm


class StatusesListView(ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'


class StatusCreateView(SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_create.html'
    success_url = '/statuses/'
    success_message = 'Статус успешно создан'


class StatusUpdateView(SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_update.html'
    success_url = '/statuses/'
    success_message = 'Статус успешно изменён'


class StatusDeleteView(SuccessMessageMixin, DeleteView):
    model = Status
    context_object_name = 'status'
    success_url = '/statuses/'
    template_name = 'statuses/status_delete.html'
    success_message = 'Статус успешно удалён'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except ProtectedError:
            messages.error(self.request, 'Невозможно удалить статус, потому что он используется')
            return HttpResponseRedirect(self.success_url)
