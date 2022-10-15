from django.test import SimpleTestCase
from django.urls import resolve, reverse
from statuses.views import StatusesListView, StatusUpdateView, StatusDeleteView, StatusCreateView


class TestUrls(SimpleTestCase):

    def test_statuses_list_url_resolves(self):
        url = reverse('statuses.list')
        self.assertEquals(resolve(url).func.view_class, StatusesListView)

    def test_status_create_url_resolves(self):
        url = reverse('status.create')
        self.assertEquals(resolve(url).func.view_class, StatusCreateView)

    def test_status_update_url_resolves(self):
        url = reverse('status.update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, StatusUpdateView)

    def test_status_delete_url_resolves(self):
        url = reverse('status.delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, StatusDeleteView)
