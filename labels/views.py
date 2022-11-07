from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from labels.models import Label
from labels.forms import LabelForm
from task_manager.mixins import LoginRequiredMessageMixin, ObjectUsedMixin


class LabelsListView(LoginRequiredMessageMixin, ListView):
    model = Label
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels'
    redirect_field_name = ''


class LabelCreateView(LoginRequiredMessageMixin,
                      SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_create.html'
    success_url = reverse_lazy('labels.list')
    success_message = _('Label created successfully')
    redirect_field_name = ''


class LabelUpdateView(LoginRequiredMessageMixin,
                      SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_update.html'
    success_url = reverse_lazy('labels.list')
    success_message = _('Label updated successfully')
    redirect_field_name = ''


class LabelDeleteView(LoginRequiredMessageMixin, ObjectUsedMixin,
                      SuccessMessageMixin, DeleteView):
    model = Label
    context_object_name = 'label'
    object_name = 'label'
    success_url = reverse_lazy('labels.list')
    template_name = 'labels/label_delete.html'
    success_message = _('Label deleted successfully')
    redirect_field_name = ''
