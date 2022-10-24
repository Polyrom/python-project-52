from django.test import TestCase, Client
from tasks.forms import TaskForm
from labels.models import Label
from statuses.models import Status
from django.contrib.auth import get_user_model


class TestForms(TestCase):
    fixtures = [
        'users.json',
        'labels.json',
        'statuses.json'
    ]

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.get(pk='1')
        self.client.force_login(self.user)
        self.label = Label.objects.get(pk='1')
        self.status = Status.objects.get(pk='1')

    def test_task_form_valid_data(self):
        form = TaskForm(data={'name': 'random',
                              'description': 'random_desc',
                              'status': self.status.pk,
                              'label': self.label.pk,
                              'executor': self.user.pk})
        self.assertTrue(form.is_valid())

    def test_task_form_no_data(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
