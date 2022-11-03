from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.db.models.deletion import ProtectedError
from django.contrib import messages
from statuses.models import Status
from statuses.forms import StatusForm
from task_manager.mixins import LoginRequiredMessageMixin


class StatusesListView(LoginRequiredMessageMixin, ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'
    redirect_field_name = ''


class StatusCreateView(LoginRequiredMessageMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_create.html'
    success_url = '/statuses/'
    success_message = 'Статус успешно создан'
    redirect_field_name = ''


class StatusUpdateView(LoginRequiredMessageMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_update.html'
    success_url = '/statuses/'
    success_message = 'Статус успешно изменён'
    redirect_field_name = ''


class StatusDeleteView(LoginRequiredMessageMixin, SuccessMessageMixin, DeleteView):
    model = Status
    context_object_name = 'status'
    success_url = '/statuses/'
    template_name = 'statuses/status_delete.html'
    success_message = 'Статус успешно удалён'
    redirect_field_name = ''

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(request, self.success_message)
            return HttpResponseRedirect(self.success_url)
        except ProtectedError:
            messages.error(
                self.request,
                'Невозможно удалить статус, потому что он используется'
            )
            return HttpResponseRedirect(self.success_url)
