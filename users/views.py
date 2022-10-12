from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from users.forms import UserCreateForm
from django.contrib.messages.views import SuccessMessageMixin


class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class SignupView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/user_create.html'

    def get_success_url(self):
        return '/login'


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    success_url = '/users'
    template_name = 'users/user_delete.html'
    success_message = 'Пользователь успешно удалён'

