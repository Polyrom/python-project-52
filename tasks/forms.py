from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'labels', 'executive')
        labels = {
            'title': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'labels': 'Метки',
            'executive': 'Исполнитель'
        }
