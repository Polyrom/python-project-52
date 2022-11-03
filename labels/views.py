from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.deletion import ProtectedError
from labels.models import Label
from labels.forms import LabelForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from task_manager.mixins import LoginRequiredMessageMixin


class LabelsListView(LoginRequiredMessageMixin, ListView):
    model = Label
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels'
    redirect_field_name = ''


class LabelCreateView(LoginRequiredMessageMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_create.html'
    success_url = '/labels/'
    success_message = 'Метка успешно создана'
    redirect_field_name = ''


class LabelUpdateView(LoginRequiredMessageMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_update.html'
    success_url = '/labels/'
    success_message = 'Метка успешно изменена'
    redirect_field_name = ''


class LabelDeleteView(LoginRequiredMessageMixin, SuccessMessageMixin, DeleteView):
    model = Label
    context_object_name = 'label'
    success_url = '/labels/'
    template_name = 'labels/label_delete.html'
    success_message = 'Метка успешно удалена'
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
                'Невозможно удалить метку, потому что она используется'
            )
            return HttpResponseRedirect(self.success_url)
