from django import forms
from tasks.models import Tasks


class TaskForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ('title', 'description', 'status', 'executive')
        labels = {
            'title': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'executive': 'Исполнитель'
        }
