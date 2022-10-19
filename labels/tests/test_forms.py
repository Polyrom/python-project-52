from django.test import TestCase
from labels.forms import LabelForm


class TestForms(TestCase):

    def test_label_form_valid_data(self):
        form = LabelForm(data={'title': 'random'})
        self.assertTrue(form.is_valid())

    def test_label_form_no_data(self):
        form = LabelForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
