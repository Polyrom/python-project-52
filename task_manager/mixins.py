from django.contrib import messages
from django.shortcuts import redirect
from task_manager import settings


class NotLoggedInMessageMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.ERROR,
                'Вы не авторизованы! Пожалуйста, выполните вход.'
            )
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)


class WrongUserMessageMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.pk == self.kwargs['pk']:
            messages.add_message(
                request, messages.ERROR,
                'У вас нет прав для изменения другого пользователя.'
            )
            return redirect('users.list')
        return super().dispatch(request, *args, **kwargs)
