from django.views.generic import ListView, CreateView
from statuses.models import Statuses
from statuses.forms import StatusForm


class StatusesListView(ListView):
    model = Statuses
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'


class StatusCreateView(CreateView):
    model = Statuses
    form_class = StatusForm
    template_name = 'statuses/status_create.html'
    success_url = '/statuses/'
