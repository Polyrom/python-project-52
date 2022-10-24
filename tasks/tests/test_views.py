from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task
from users.models import User
from labels.models import Label
from statuses.models import Status


class TestViews(TestCase):
    fixtures = [
        'users.json',
        'tasks.json',
        'labels.json',
        'statuses.json'
    ]

    def setUp(self):
        self.client = Client()
        self.user = User.objects.get(pk='1')
        self.client.force_login(user=self.user)
        self.label = Label.objects.get(pk='1')
        self.status = Status.objects.get(pk='1')
        self.tasks_list = reverse('tasks.list')
        self.create_task = reverse('task.create')
        self.update_task = reverse('task.update', kwargs={'pk': 1})
        self.delete_task = reverse('task.delete', kwargs={'pk': 1})

    def test_tasks_list(self):
        response = self.client.get(self.tasks_list)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks_list.html')

    def test_create_task_template(self):
        response = self.client.get(self.create_task)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_create.html')

    def test_create_task(self):
        data = {
            'name': 'random',
            'status': self.status.pk,
            'label': self.label.pk,
            'executor': self.user.pk
        }
        response = self.client.post(self.create_task, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Task.objects.count(), 2)

    def test_update_task_template(self):
        response = self.client.get(self.update_task)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_update.html')

    def test_delete_task_GET(self):
        response = self.client.get(self.delete_task)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_delete.html')

    def test_delete_task_POST(self):
        response = self.client.delete(self.delete_task)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Task.objects.count(), 0)
