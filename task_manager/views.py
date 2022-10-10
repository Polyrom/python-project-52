from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginInterfaceView(LoginView):
    template_name = 'registration/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'registration/logout.html'
