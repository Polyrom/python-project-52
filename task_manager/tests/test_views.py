from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.home = reverse('home')
        self.login = reverse('login')
        self.logout = reverse('logout')

    def test_home_page(self):
        response = self.client.get(self.home)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_page_GET(self):
        response = self.client.get(self.login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_page_POST(self):
        user = User.objects.create(
            pk=1,
            username='Boss',
            first_name='Michael',
            last_name='Scott'
        )
        user.set_password('12345')
        user.save()
        data = {'username': 'Boss', 'password': '12345'}
        response = self.client.post(self.login, data=data)
        self.assertEquals(response.status_code, 302)
        self.assertIn('_auth_user_id', self.client.session)

    def test_logout_page_POST(self):
        user = User.objects.create_user(username='random')
        self.client.force_login(user=user)
        response = self.client.post(self.logout)
        self.assertEquals(response.status_code, 302)
