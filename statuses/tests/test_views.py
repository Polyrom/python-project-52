import os
import json
from django.test import TestCase, Client
from django.urls import reverse
from statuses.models import Status
from django.contrib.auth import get_user_model

NEW_OBJECTS_PATH = os.path.join('task_manager',
                                'fixtures',
                                'new_objects.json')


class TestViews(TestCase):
    fixtures = ['users.json', 'statuses.json']

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.get(pk=1)
        self.client.force_login(self.user)
        self.status = Status.objects.get(pk=1)
        self.statuses_list_url = reverse('statuses.list')
        self.create_status_url = reverse('status.create')
        self.update_status_url = reverse('status.update', kwargs={'pk': 1})
        self.delete_status_url = reverse('status.delete', kwargs={'pk': 1})

    def test_statuses_list(self):
        response = self.client.get(self.statuses_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses_list.html')

    def test_create_status_template(self):
        response = self.client.get(self.create_status_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/status_create.html')

    def test_create_status(self):
        with open(NEW_OBJECTS_PATH, 'rb') as new_objects:
            data = json.load(new_objects)['status']
            response = self.client.post(self.create_status_url, data=data)
            self.assertEquals(response.status_code, 302)
            self.assertEquals(Status.objects.count(), 2)

    def test_update_status_template(self):
        response = self.client.get(self.update_status_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/status_update.html')

    def test_update_status(self):
        with open(NEW_OBJECTS_PATH, 'rb') as new_objects:
            data = json.load(new_objects)['status']
            response = self.client.post(self.update_status_url, data=data)
            self.assertEquals(response.status_code, 302)
            self.assertEquals(Status.objects.get(pk=1).name, 'random')

    def test_delete_status_template(self):
        response = self.client.get(self.delete_status_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/status_delete.html')

    def test_delete_status(self):
        response = self.client.delete(self.delete_status_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Status.objects.count(), 0)
