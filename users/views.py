from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView, UpdateView
from users.forms import UserCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


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
    login_url = '/login/'
    success_message = 'Пользователь успешно изменён'
    permission_denied_message = 'Вы не авторизованы! Пожалуйста, выполните вход.'
    redirect_field_name = ''

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR,
                                 self.permission_denied_message)
            return self.handle_no_permission()
        return super().dispatch(
            request, *args, **kwargs
        )


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    success_url = '/users'
    template_name = 'users/user_delete.html'
    login_url = '/login/'
    success_message = 'Пользователь успешно удалён'

