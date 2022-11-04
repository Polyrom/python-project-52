from django import forms
from labels.models import Label
from django.utils.translation import gettext_lazy as _


class LabelForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ('name',)
        labels = {
            'name': _('Name')
        }
