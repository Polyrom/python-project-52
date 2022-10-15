from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView, UpdateView
from users.forms import UserCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class SignupView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/user_create.html'

    def get_success_url(self):
        return '/login'


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/user_update.html'
    success_url = '/users/'
    success_message = 'Пользователь успешно изменён'
    redirect_field_name = ''

    # add custom permission_denied_message
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 'Вы не авторизованы! Пожалуйста, выполните вход.')
        elif not request.user.pk == self.kwargs['pk']:
            messages.add_message(request, messages.ERROR,
                                 'У вас нет прав для изменения другого пользователя.')
            return redirect('users.list')
        return response


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    success_url = '/users'
    template_name = 'users/user_delete.html'
    success_message = 'Пользователь успешно удалён'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if not request.user.pk == self.kwargs['pk']:
            messages.add_message(request, messages.ERROR,
                                 'У вас нет прав для изменения другого пользователя.')
            return redirect('users.list')
        return response


