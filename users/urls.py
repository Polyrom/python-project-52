from django.urls import path
from users.views import UsersListView, SignupView


urlpatterns = [
    path('', UsersListView.as_view(), name='users.list'),
    path('create/', SignupView.as_view(), name='user.create'),
]