from django.urls import path
from users.views import (UsersListView, SignupView,
                         UserDeleteView, UserUpdateView)


urlpatterns = [
    path('', UsersListView.as_view(), name='users.list'),
    path('create/', SignupView.as_view(), name='user.create'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user.delete'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user.update'),
]
