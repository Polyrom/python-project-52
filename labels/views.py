from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.deletion import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin
from labels.models import Label
from labels.forms import LabelForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from task_manager.mixins import NotLoggedInMessageMixin


class LabelsListView(NotLoggedInMessageMixin, LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels'


class LabelCreateView(NotLoggedInMessageMixin, LoginRequiredMixin,
                      SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_create.html'
    success_url = '/labels/'
    success_message = 'Метка успешно создана'


class LabelUpdateView(NotLoggedInMessageMixin, LoginRequiredMixin,
                      SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_update.html'
    success_url = '/labels/'
    success_message = 'Метка успешно изменена'


class LabelDeleteView(NotLoggedInMessageMixin, LoginRequiredMixin,
                      SuccessMessageMixin, DeleteView):
    model = Label
    context_object_name = 'label'
    success_url = '/labels/'
    template_name = 'labels/label_delete.html'
    success_message = 'Метка успешно удалена'

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
