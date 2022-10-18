from django.test import TestCase, Client
from django.urls import reverse
from statuses.models import Status
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='random')
        self.client.force_login(user=self.user)
        self.statuses_list = reverse('statuses.list')
        self.create_status = reverse('status.create')
        self.update_status = reverse('status.update', kwargs={'pk': 1})
        self.delete_status = reverse('status.delete', kwargs={'pk': 1})

    def test_statuses_list(self):
        response = self.client.get(self.statuses_list)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses_list.html')

    def test_create_status_GET(self):
        response = self.client.get(self.create_status)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/status_create.html')

    def test_create_status_POST(self):
        data = {'title': 'random'}
        response = self.client.post(self.create_status, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Status.objects.count(), 1)

    def test_update_status_GET(self):
        Status.objects.create(pk=1, title='title')
        response = self.client.get(self.update_status)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/status_update.html')

    def test_update_status_POST(self):
        Status.objects.create(pk=1, title='title')
        data = {'title': 'random'}
        response = self.client.post(self.update_status, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Status.objects.get(pk=1).title, 'random')

    def test_delete_status_GET(self):
        Status.objects.create(pk=1, title='title')
        response = self.client.get(self.delete_status)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/status_delete.html')

    def test_delete_status_POST(self):
        Status.objects.create(pk=1, title='title')
        response = self.client.delete(self.delete_status)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Status.objects.count(), 0)
