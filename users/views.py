from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from users.forms import UserCreateForm
from task_manager.mixins import WrongUserMessageMixin, ObjectUsedMixin


class UsersListView(ListView):
    model = get_user_model()
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class SignupView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'users/user_create.html'
    success_message = _('User signed up successfully')

    def get_success_url(self):
        return '/login'


class UserUpdateView(WrongUserMessageMixin,
                     SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = UserCreateForm
    template_name = 'users/user_update.html'
    success_url = '/users/'
    success_message = _('User updated successfully')
    redirect_field_name = ''


class UserDeleteView(WrongUserMessageMixin, ObjectUsedMixin,
                     SuccessMessageMixin, DeleteView):
    model = get_user_model()
    object_name = 'user'
    success_url = '/users/'
    template_name = 'users/user_delete.html'
    success_message = _('User deleted successfully')
    redirect_field_name = ''
