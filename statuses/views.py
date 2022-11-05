from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from task_manager.mixins import LoginRequiredMessageMixin, ObjectUsedMixin
from statuses.models import Status
from statuses.forms import StatusForm


class StatusesListView(LoginRequiredMessageMixin, ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'
    redirect_field_name = ''


class StatusCreateView(LoginRequiredMessageMixin,
                       SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_create.html'
    success_url = '/statuses/'
    success_message = _('Status created successfully')
    redirect_field_name = ''


class StatusUpdateView(LoginRequiredMessageMixin,
                       SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_update.html'
    success_url = '/statuses/'
    success_message = _('Status updated successfully')
    redirect_field_name = ''


class StatusDeleteView(LoginRequiredMessageMixin, ObjectUsedMixin,
                       SuccessMessageMixin, DeleteView):
    model = Status
    context_object_name = 'status'
    object_name = 'status'
    success_url = '/statuses/'
    template_name = 'statuses/status_delete.html'
    success_message = _('Status deleted successfully')
    redirect_field_name = ''
