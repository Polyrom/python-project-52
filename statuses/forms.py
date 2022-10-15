from django import forms
from statuses.models import Statuses


class StatusForm(forms.ModelForm):

    class Meta:
        model = Statuses
        fields = ('title',)
        labels = {
            'title': 'Имя'
        }
