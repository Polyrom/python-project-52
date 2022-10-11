from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginInterfaceView(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_message = 'Вы залогинены'


class LogoutInterfaceView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Вы разлогинены')
        return response
