from django import forms
from statuses.models import Status
from django.utils.translation import gettext_lazy as _


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('name',)
        labels = {
            'name': _('Name')
        }
