from django.test import SimpleTestCase
from django.urls import resolve, reverse
from users.views import (UsersListView, SignupView,
                         UserUpdateView, UserDeleteView)


class TestUrls(SimpleTestCase):

    def test_users_list_url_resolves(self):
        url = reverse('users.list')
        self.assertEquals(resolve(url).func.view_class, UsersListView)

    def test_signup_url_resolves(self):
        url = reverse('user.create')
        self.assertEquals(resolve(url).func.view_class, SignupView)

    def test_user_update_url_resolves(self):
        url = reverse('user.update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, UserUpdateView)

    def test_user_delete_url_resolves(self):
        url = reverse('user.delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, UserDeleteView)
