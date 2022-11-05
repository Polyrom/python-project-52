from django.test import TestCase, Client
from django.urls import reverse
from labels.models import Label
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    fixtures = ['users.json', 'labels.json']

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.get(pk='1')
        self.client.force_login(user=self.user)
        self.label = Label.objects.get(pk='1')
        self.labels_list_url = reverse('labels.list')
        self.create_label_url = reverse('label.create')
        self.update_label_url = reverse('label.update', kwargs={'pk': 1})
        self.delete_label_url = reverse('label.delete', kwargs={'pk': 1})

    def test_labels_list(self):
        response = self.client.get(self.labels_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/labels_list.html')

    def test_create_label_template(self):
        response = self.client.get(self.create_label_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/label_create.html')

    def test_create_label(self):
        data = {'name': 'random'}
        response = self.client.post(self.create_label_url, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Label.objects.count(), 2)

    def test_update_label_template(self):
        response = self.client.get(self.update_label_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/label_update.html')

    def test_update_label(self):
        data = {'name': 'random'}
        response = self.client.post(self.update_label_url, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Label.objects.get(pk=1).name, 'random')

    def test_delete_label_template(self):
        response = self.client.get(self.delete_label_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/label_delete.html')

    def test_delete_status(self):
        response = self.client.delete(self.delete_label_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Label.objects.count(), 0)
