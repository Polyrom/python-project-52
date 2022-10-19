from django.test import TestCase, Client
from django.urls import reverse
from labels.models import Label
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='random')
        self.client.force_login(user=self.user)
        self.labels_list = reverse('labels.list')
        self.create_label = reverse('label.create')
        self.update_label = reverse('label.update', kwargs={'pk': 1})
        self.delete_label = reverse('label.delete', kwargs={'pk': 1})

    def test_labels_list(self):
        response = self.client.get(self.labels_list)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/labels_list.html')

    def test_create_label_GET(self):
        response = self.client.get(self.create_label)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/label_create.html')

    def test_create_label_POST(self):
        data = {'title': 'random'}
        response = self.client.post(self.create_label, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Label.objects.count(), 1)

    def test_update_label_GET(self):
        Label.objects.create(pk=1, title='title')
        response = self.client.get(self.update_label)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/label_update.html')

    def test_update_label_POST(self):
        Label.objects.create(pk=1, title='title')
        data = {'title': 'random'}
        response = self.client.post(self.update_label, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Label.objects.get(pk=1).title, 'random')

    def test_delete_label_GET(self):
        Label.objects.create(pk=1, title='title')
        response = self.client.get(self.delete_label)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/label_delete.html')

    def test_delete_status_POST(self):
        Label.objects.create(pk=1, title='title')
        response = self.client.delete(self.delete_label)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Label.objects.count(), 0)