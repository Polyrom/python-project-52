import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasks.models import Task
from labels.models import Label
from statuses.models import Status
from task_manager.settings import NEW_OBJECTS_PATH


class TestViews(TestCase):
    fixtures = [
        'users.json',
        'tasks.json',
        'labels.json',
        'statuses.json'
    ]

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.get(pk='1')
        self.client.force_login(user=self.user)
        self.label = Label.objects.get(pk='1')
        self.status = Status.objects.get(pk='1')
        self.tasks_list_url = reverse('tasks.list')
        self.create_task_url = reverse('task.create')
        self.update_task_url = reverse('task.update', kwargs={'pk': 1})
        self.delete_task_url = reverse('task.delete', kwargs={'pk': 1})

    def test_tasks_list(self):
        response = self.client.get(self.tasks_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks_list.html')

    def test_create_task_template(self):
        response = self.client.get(self.create_task_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_create.html')

    def test_create_task(self):
        with open(NEW_OBJECTS_PATH, 'rb') as new_objects:
            data = json.load(new_objects)['task']
            response = self.client.post(self.create_task_url, data=data)
            self.assertEquals(response.status_code, 302)
            self.assertEquals(Task.objects.count(), 2)

    def test_update_task_template(self):
        response = self.client.get(self.update_task_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_update.html')

    def test_update_task(self):
        with open(NEW_OBJECTS_PATH, 'rb') as new_objects:
            data = json.load(new_objects)['task']
            response = self.client.post(self.update_task_url, data=data)
            self.assertEquals(response.status_code, 302)
            self.assertEquals(Task.objects.get(pk=1).name, 'random')

    def test_delete_task_template(self):
        response = self.client.get(self.delete_task_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_delete.html')

    def test_delete_task(self):
        response = self.client.delete(self.delete_task_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Task.objects.count(), 0)
