from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, tag

from account.form import *


class TestCustomUserCreationForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()

        cls.username = 'test'
        cls.email = 'test@test.com'
        cls.password = User.objects.make_random_password()
        cls.birth_date = datetime.now()

    @tag('fast')
    def test_valid_data(self):
        data = {
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'birth_date': self.birth_date
        }
        form = CustomUserCreationForm(data=data)
        self.assertTrue(form.is_valid())

    @tag('fast')
    def test_no_data(self):
        form = CustomUserCreationForm()
        self.assertFalse(form.is_valid())

    @tag('fast')
    def test_different_password(self):
        data = {
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': User.objects.make_random_password(),
            'birth_date': self.birth_date
        }
        form = CustomUserCreationForm(data=data)
        self.assertFalse(form.is_valid())
