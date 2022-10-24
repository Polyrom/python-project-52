from django.views.generic import ListView, CreateView
from django.db.models.deletion import ProtectedError
from django.views.generic.edit import DeleteView, UpdateView
from users.forms import UserCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import NotLoggedInMessageMixin, WrongUserMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model


class UsersListView(ListView):
    model = get_user_model()
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class SignupView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'users/user_create.html'
    success_message = 'Пользователь успешно зарегистрирован'

    def get_success_url(self):
        return '/login'


class UserUpdateView(SuccessMessageMixin, NotLoggedInMessageMixin,
                     WrongUserMessageMixin, UpdateView):
    model = get_user_model()
    form_class = UserCreateForm
    template_name = 'users/user_update.html'
    success_url = '/users/'
    success_message = 'Пользователь успешно изменён'


class UserDeleteView(SuccessMessageMixin, NotLoggedInMessageMixin,
                     WrongUserMessageMixin, DeleteView):
    model = get_user_model()
    success_url = '/users'
    template_name = 'users/user_delete.html'
    success_message = 'Пользователь успешно удалён'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(request, self.success_message)
            return HttpResponseRedirect(self.success_url)
        except ProtectedError:
            messages.error(
                request,
                'Невозможно удалить пользователя, потому что он используется'
            )
            return HttpResponseRedirect(self.success_url)
