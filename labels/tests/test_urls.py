from django.test import SimpleTestCase
from django.urls import resolve, reverse
from labels.views import LabelsListView, LabelCreateView, LabelUpdateView, LabelDeleteView


class TestUrls(SimpleTestCase):

    def test_statuses_list_url_resolves(self):
        url = reverse('labels.list')
        self.assertEquals(resolve(url).func.view_class, LabelsListView)

    def test_status_create_url_resolves(self):
        url = reverse('label.create')
        self.assertEquals(resolve(url).func.view_class, LabelCreateView)

    def test_status_update_url_resolves(self):
        url = reverse('label.update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, LabelUpdateView)

    def test_status_delete_url_resolves(self):
        url = reverse('label.delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, LabelDeleteView)
