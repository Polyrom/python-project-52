from django.contrib import messages
from django.shortcuts import redirect
from django.db.models.deletion import ProtectedError
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from task_manager import settings


class LoginRequiredMessageMixin(UserPassesTestMixin):

    login_required_message = _('You are not logged in! Please log in.')

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.add_message(
            self.request, messages.ERROR,
            self.login_required_message
        )
        return redirect(settings.LOGIN_URL)


class WrongUserMessageMixin(LoginRequiredMessageMixin):

    wrong_user_message = _('You are not allowed to update other users')

    def test_func(self):
        return super().test_func and (self.request.user.pk == self.kwargs['pk'])

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        messages.add_message(
            self.request, messages.ERROR,
            self.wrong_user_message
        )
        return redirect(self.success_url)


class UserMatchesAuthorMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user == self.model.objects.get(id=kwargs['pk']).author:
            messages.add_message(
                request, messages.ERROR,
                _('Task can be deleted only by its author')
            )
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class ObjectUsedMixin:

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(request, self.success_message)
            return HttpResponseRedirect(self.success_url)
        except ProtectedError:
            messages.error(
                request,
                _(f'Impossible to delete {self.object_name} as it is used')
            )
            return HttpResponseRedirect(self.success_url)
