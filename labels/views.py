from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.deletion import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin
from labels.models import Label
from labels.forms import LabelForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from task_manager import settings


class LabelsListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.ERROR,
                'Вы не авторизованы! Пожалуйста, выполните вход.'
            )
            return redirect(settings.LOGIN_URL)
        return response


class LabelCreateView(SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_create.html'
    success_url = '/labels/'
    success_message = 'Метка успешно создана'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.ERROR,
                'Вы не авторизованы! Пожалуйста, выполните вход.'
            )
            return redirect(settings.LOGIN_URL)
        return response


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_update.html'
    success_url = '/labels/'
    success_message = 'Метка успешно изменена'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.ERROR,
                'Вы не авторизованы! Пожалуйста, выполните вход.'
            )
            return redirect(settings.LOGIN_URL)
        return response


class LabelDeleteView(SuccessMessageMixin, DeleteView):
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

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.ERROR,
                'Вы не авторизованы! Пожалуйста, выполните вход.'
            )
            return redirect(settings.LOGIN_URL)
        return response
