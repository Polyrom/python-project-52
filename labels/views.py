from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from labels.models import Labels
from labels.forms import LabelForm


class LabelsListView(ListView):
    model = Labels
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels'


class LabelCreateView(SuccessMessageMixin, CreateView):
    model = Labels
    form_class = LabelForm
    template_name = 'labels/label_create.html'
    success_url = '/labels/'
    success_message = 'Метка успешно создана'


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    model = Labels
    form_class = LabelForm
    template_name = 'labels/label_update.html'
    success_url = '/labels/'
    success_message = 'Метка успешно изменена'


class LabelDeleteView(SuccessMessageMixin, DeleteView):
    model = Labels
    context_object_name = 'label'
    success_url = '/labels/'
    template_name = 'labels/label_delete.html'
    success_message = 'Метка успешно удалена'
