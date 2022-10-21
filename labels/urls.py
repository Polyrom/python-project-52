from django.urls import path
from labels.views import (LabelsListView, LabelCreateView,
                          LabelUpdateView, LabelDeleteView)


urlpatterns = [
    path('', LabelsListView.as_view(), name='labels.list'),
    path('create/', LabelCreateView.as_view(), name='label.create'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='label.update'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='label.delete'),
]
