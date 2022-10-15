from django.test import TestCase
from statuses.forms import StatusForm


class TestForms(TestCase):

    def test_status_form_valid_data(self):
        form = StatusForm(data={'title': 'random'})
        self.assertTrue(form.is_valid())

    def test_status_form_no_data(self):
        form = StatusForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
