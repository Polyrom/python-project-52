from django.test import TestCase, Client
from tasks.forms import TaskForm
from labels.models import Label
from statuses.models import Status
from users.models import User


class TestForms(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='random_user')
        self.client.force_login(user=self.user)
        self.label = Label.objects.create(name='random_label')
        self.status = Status.objects.create(name='random_status')

    def test_task_form_valid_data(self):
        form = TaskForm(data={'name': 'random',
                              'description': 'random_desc',
                              'status': self.status.pk,
                              'label': ['1'],
                              'executor': self.user.pk})
        self.assertTrue(form.is_valid())

    def test_task_form_no_data(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
