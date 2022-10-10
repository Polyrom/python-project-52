from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/user_create.html'

    def get_success_url(self):
        return '/login'
