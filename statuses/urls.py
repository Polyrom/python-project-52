from django.urls import path
from statuses.views import StatusesListView, StatusCreateView


urlpatterns = [
    path('', StatusesListView.as_view(), name='statuses.list'),
    path('create/', StatusCreateView.as_view(), name='status.create'),
]
