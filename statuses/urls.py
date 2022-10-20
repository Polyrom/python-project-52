from django.urls import path
from statuses.views import StatusesListView, StatusCreateView, StatusUpdateView, StatusDeleteView


urlpatterns = [
    path('', StatusesListView.as_view(), name='statuses.list'),
    path('create/', StatusCreateView.as_view(), name='status.create'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='status.update'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status.delete'),
]
