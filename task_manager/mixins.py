from django.contrib import messages
from django.shortcuts import redirect
from task_manager import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext_lazy as _


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
