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
        self.user.set_password('12345')
        self.user.save()

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

    def test_signup_POST(self):
        data = {
            'first_name': 'Dwight',
            'last_name': 'Shrute',
            'username': 'BestSalesman',
            'password1': 'scranton',
            'password2': 'scranton'
        }
        response = self.client.post(self.create_user, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 2)

    def test_update_user_GET_correct_user(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.update_user)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_update.html')

    def test_update_user_GET_wrong_user(self):
        response = self.client.get(self.update_user)
        self.assertEquals(response.status_code, 302)

    def test_update_user_POST(self):
        self.client.force_login(user=self.user)
        data = {
            'first_name': 'Michael',
            'last_name': 'Scott',
            'username': 'RegionalManager',
            'password1': '12345',
            'password2': '12345'
        }
        response = self.client.post(self.update_user, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.first().username, 'RegionalManager')

    def test_delete_user_GET(self):
        response = self.client.get(self.delete_user)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_delete.html')

    def test_delete_user_POST(self):
        response = self.client.delete(self.delete_user)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 0)
