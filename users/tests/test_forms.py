from django.test import TestCase
from users.forms import UserCreateForm


class TestForms(TestCase):

    def test_user_create_form_valid_data(self):
        form = UserCreateForm(data={
            'first_name': 'Michael',
            'last_name': 'Scott',
            'username': 'RegionalManager',
            'password1': '12345',
            'password2': '12345'
        })

        self.assertTrue(form.is_valid())

    def test_user_create_form_no_data(self):
        form = UserCreateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
