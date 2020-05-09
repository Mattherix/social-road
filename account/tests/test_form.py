from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, tag
from django.core.files.uploadedfile import SimpleUploadedFile

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


class TestCustomAuthenticationForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()

        cls.username = 'test'
        cls.email = 'test@test.com'
        cls.password = User.objects.make_random_password()
        cls.birth_date = datetime.now()

        cls.user = User.objects.create_user(
            username=cls.username,
            email=cls.email,
            password=cls.password,
            birth_date=datetime.now()
        )

    @tag('fast')
    def test_valid_data(self):
        data = {
            'username': self.username,
            'password': self.password
        }
        form = CustomAuthenticationForm(data=data)

        self.assertTrue(form.is_valid())

    @tag('fast')
    def test_no_data(self):
        form = CustomAuthenticationForm()
        self.assertFalse(form.is_valid())

    @tag('fast')
    def test_wrong_password(self):
        data = {
            'username': self.username,
            'password': User.objects.make_random_password(),
        }
        form = CustomAuthenticationForm(data=data)
        self.assertFalse(form.is_valid())

class TestCustomUserChangeForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()

        cls.username = 'test'
        cls.email = 'test@test.com'
        cls.password = User.objects.make_random_password()
        cls.birth_date = datetime.now()
        cls.bio = 'flsekfhoqsjfgsjdgfj '
        cls.slug = cls.username
        cls.image = SimpleUploadedFile(
            name='TUX.png',
            content=open('account/tests/TUX.png', 'rb').read(),
            content_type='image/png'
        )

        cls.user = User.objects.create_user(
            username=cls.username,
            email=cls.email,
            password=cls.password,
            birth_date=datetime.now()
        )

    @tag('fast')
    def test_valid_data(self):
        data = {
            'email': self.email,
            'birth_date': self.birth_date,
            'bio': self.bio,
            'image': self.image
        }
        print(data)
        form = CustomUserChangeForm(data=data)

        self.assertTrue(form.is_valid())
