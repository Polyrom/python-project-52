from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.get(pk='1')
        self.home_url = reverse('home')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

    def test_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_page_template(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_page(self):
        self.user.set_password('12345')
        self.user.save()
        data = {'username': 'Boss', 'password': '12345'}
        response = self.client.post(self.login_url, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertIn('_auth_user_id', self.client.session)

    def test_logout_page(self):
        self.client.force_login(self.user)
        response = self.client.post(self.logout_url)
        self.assertEquals(response.status_code, 302)
