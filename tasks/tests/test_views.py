from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task
from users.models import User
from labels.models import Label
from statuses.models import Status


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(pk=1, username='random')
        self.client.force_login(user=self.user)
        self.tasks_list = reverse('tasks.list')
        self.create_task = reverse('task.create')
        self.update_task = reverse('task.update', kwargs={'pk': 1})
        self.delete_task = reverse('task.delete', kwargs={'pk': 1})
        self.label = Label.objects.create(name='random_label')
        self.status = Status.objects.create(name='random_status')

    def test_tasks_list(self):
        response = self.client.get(self.tasks_list)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks_list.html')

    def test_create_task_GET(self):
        response = self.client.get(self.create_task)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_create.html')

    def test_create_task_POST(self):
        data = {
            'name': 'random',
            'status': self.status.pk,
            'label': ['1'],
            'executor': self.user.pk
        }
        response = self.client.post(self.create_task, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Task.objects.count(), 1)

    def test_update_task_GET(self):
        Task.objects.create(
            author=self.user,
            executor=self.user
        )
        response = self.client.get(self.update_task)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_update.html')

    def test_delete_task_GET(self):
        Task.objects.create(
            author=self.user,
            executor=self.user
        )
        response = self.client.get(self.delete_task)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_delete.html')

    def test_delete_task_POST(self):
        Task.objects.create(
            author=self.user,
            executor=self.user
        )
        response = self.client.delete(self.delete_task)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Task.objects.count(), 0)
