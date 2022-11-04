from django import forms
from django.contrib.auth import get_user_model
from django_filters import FilterSet, ChoiceFilter, BooleanFilter
from django.db.models import Value
from django.db.models.functions import Concat
from django.utils.translation import gettext_lazy as _

from tasks.models import Task
from statuses.models import Status
from labels.models import Label


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }


class TaskFilter(FilterSet):

    all_statuses = Status.objects.values_list('id', 'name', named=True).all()
    status = ChoiceFilter(label=_('Status'), choices=all_statuses)
    user = get_user_model()
    all_executors = user.objects.values_list(
        'id',
        Concat('first_name', Value(' '), 'last_name'),
        named=True).all()
    executor = ChoiceFilter(label=_('Executor'), choices=all_executors)
    all_labels = Label.objects.values_list('id', 'name', named=True).all()
    labels = ChoiceFilter(label=_('Label'), choices=all_labels)
    my_tasks = BooleanFilter(
        label=_('Only my tasks'),
        widget=forms.CheckboxInput(),
        method='filter_self_task',
        field_name='my_task',
    )

    def filter_self_task(self, queryset, name, value):
        return queryset.filter(author=self.request.user) if value else queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
