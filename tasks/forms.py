from django import forms
from django_filters import FilterSet, ChoiceFilter, BooleanFilter
from django.db.models import Value
from django.db.models.functions import Concat
from tasks.models import Task
from statuses.models import Status
from labels.models import Label
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'label')
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'executor': 'Исполнитель',
            'label': 'Метки',
        }


class TaskFilter(FilterSet):

    all_statuses = Status.objects.values_list('id', 'name', named=True).all()
    status = ChoiceFilter(label='Статус', choices=all_statuses)
    all_executors = User.objects.values_list(
        'id',
        Concat('first_name', Value(' '), 'last_name'),
        named=True).all()
    executor = ChoiceFilter(label='Исполнитель', choices=all_executors)
    all_labels = Label.objects.values_list('id', 'name', named=True).all()
    label = ChoiceFilter(label='Метка', choices=all_labels)
    my_tasks = BooleanFilter(
        label='Только свои задачи',
        widget=forms.CheckboxInput(),
        method='filter_self_task',
        field_name='my_task',
    )

    def filter_self_task(self, queryset, name, value):
        return queryset.filter(author=self.request.user) if value else queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label']
