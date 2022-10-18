from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.db.models.deletion import ProtectedError
from django.contrib import messages
from statuses.models import Status
from statuses.forms import StatusForm
from django.shortcuts import redirect


class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'
    login_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect(self.login_url)
        return response


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_create.html'
    success_url = '/statuses/'
    success_message = 'Статус успешно создан'
    login_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect(self.login_url)
        return response


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_update.html'
    success_url = '/statuses/'
    success_message = 'Статус успешно изменён'
    login_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect(self.login_url)
        return response


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    context_object_name = 'status'
    success_url = '/statuses/'
    template_name = 'statuses/status_delete.html'
    success_message = 'Статус успешно удалён'
    login_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect(self.login_url)
        return response

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except ProtectedError:
            messages.error(self.request, 'Невозможно удалить статус, потому что он используется')
            return HttpResponseRedirect(self.success_url)
