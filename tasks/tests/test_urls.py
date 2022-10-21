from django.test import SimpleTestCase
from django.urls import resolve, reverse
from tasks.views import (TasksListView, TaskCreateView,
                         TaskUpdateView, TaskDeleteView, TaskDetailsView)


class TestUrls(SimpleTestCase):

    def test_tasks_list_url_resolves(self):
        url = reverse('tasks.list')
        self.assertEquals(resolve(url).func.view_class, TasksListView)

    def test_task_create_url_resolves(self):
        url = reverse('task.create')
        self.assertEquals(resolve(url).func.view_class, TaskCreateView)

    def test_task_update_url_resolves(self):
        url = reverse('task.update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, TaskUpdateView)

    def test_task_delete_url_resolves(self):
        url = reverse('task.delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, TaskDeleteView)

    def test_task_details_url_resolves(self):
        url = reverse('task.details', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, TaskDetailsView)
