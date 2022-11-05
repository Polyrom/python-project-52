import os
import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

NEW_OBJECTS_PATH = os.path.join('task_manager',
                                'fixtures',
                                'new_objects.json')


class TestViews(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.get(pk=1)
        self.users_list_url = reverse('users.list')
        self.create_user_url = reverse('user.create')
        self.delete_user_url = reverse('user.delete', kwargs={'pk': 1})
        self.update_user_url = reverse('user.update', kwargs={'pk': 1})

    def test_users_list(self):
        response = self.client.get(self.users_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users_list.html')

    def test_signup_template(self):
        response = self.client.get(self.create_user_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_create.html')

    def test_signup(self):
        with open(NEW_OBJECTS_PATH, 'rb') as new_objects:
            user_data = json.load(new_objects)['new_user']
            response = self.client.post(self.create_user_url, data=user_data)
            self.assertEquals(response.status_code, 302)
            self.assertEquals(get_user_model().objects.count(), 2)
            self.assertEquals(get_user_model().objects.get(pk=2).username,
                              'BestSalesman')

    def test_update_user_template_correct_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.update_user_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_update.html')

    def test_update_user_template_wrong_user(self):
        response = self.client.get(self.update_user_url)
        self.assertEquals(response.status_code, 302)

    def test_update_user(self):
        with open(NEW_OBJECTS_PATH, 'rb') as new_objects:
            self.client.force_login(self.user)
            new_user_data = json.load(new_objects)['update_user_info']
            response = self.client.post(self.update_user_url,
                                        data=new_user_data)
            self.assertEquals(response.status_code, 302)
            self.assertEquals(
                get_user_model().objects.first().username,
                'RegionalManager'
            )

    def test_delete_user_template(self):
        self.client.force_login(self.user)
        response = self.client.get(self.delete_user_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_delete.html')

    def test_delete_user(self):
        self.client.force_login(self.user)
        response = self.client.delete(self.delete_user_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(get_user_model().objects.count(), 0)
