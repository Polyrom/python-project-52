from django.test import SimpleTestCase
from task_manager.views import HomeView, LoginInterfaceView, LogoutInterfaceView
from django.urls import resolve, reverse


class TestUrls(SimpleTestCase):

    def test_home_page_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_login_page_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginInterfaceView)

    def test_logout_page_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutInterfaceView)
