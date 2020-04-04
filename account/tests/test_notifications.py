from django.test import TestCase, tag

from account.models.notifications import *


class TestNotification(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.password = User.objects.make_random_password()
        cls.user = User.objects.create_user(
            username='Johny Doe',
            email='Johny@doe.com',
            password=cls.password
        )
        cls.password_creator = User.objects.make_random_password()
        cls.creator = User.objects.create_user(
            username='Bill Doe',
            email='bill@doe.com',
            password=cls.password_creator
        )
        cls.post = Post.objects.create(
            creator=cls.creator,
            title='Article #1',
        )
        cls.type = 'S'
        cls.message = 'Bienvenue sur social-road'
        cls.notification = Notification.objects.create(
            user=cls.user,
            post=cls.post,
            type=cls.type,
            level=3,
            message=cls.message
        )

    @tag('fast')
    def test_str_method(self):
        self.assertEqual(str(self.notification), self.message)
