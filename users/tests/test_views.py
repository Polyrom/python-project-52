from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            pk=1,
            username='Boss',
            first_name='Michael',
            last_name='Scott'
        )
        self.client.force_login(user=self.user)
        self.users_list = reverse('users.list')
        self.create_user = reverse('user.create')
        self.delete_user = reverse('user.delete', kwargs={'pk': 1})
        self.update_user = reverse('user.update', kwargs={'pk': 1})

    def test_users_list(self):
        response = self.client.get(self.users_list)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users_list.html')

    def test_signup_GET(self):
        response = self.client.get(self.create_user)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_create.html')

    def test_delete_user_GET(self):
        response = self.client.get(self.delete_user)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_delete.html')

    def test_update_user_GET(self):
        response = self.client.get(self.update_user)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_update.html')
