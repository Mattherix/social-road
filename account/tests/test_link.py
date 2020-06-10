from django.test import TestCase, tag

from account.models.link import *


class TestSocialLink(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.password = User.objects.make_random_password()
        cls.user = User.objects.create_user(
            username='John Doe',
            email='John@doe.com',
            password=cls.password
        )
        cls.username = 'John Doe'
        cls.network = 'F'
        cls.link = SocialLink.objects.create(
            user=cls.user,
            network=cls.network,
            username=cls.username
        )

    @tag('fast')
    def test_str_method(self):
        self.assertEqual(str(self.link), self.user.username + ' is ' + self.username + ' on ' + self.network)

    @tag('fast')
    def test_url(self):
        self.assertEqual(self.link.url, 'https://www.facebook.com/John Doe')
        self.link.network = 'Y'
        self.assertEqual(self.link.url, 'https://www.youtube.com/user/John Doe')
        self.link.network = 'I'
        self.assertEqual(self.link.url, 'https://www.instagram.com/John Doe/')
        self.link.network = 'Tw'
        self.assertEqual(self.link.url, 'https://twitter.com/John Doe')
        self.link.network = 'S'
        self.assertEqual(self.link.url, 'snapchat://add/John Doe')
        self.link.network = 'P'
        self.assertEqual(self.link.url, 'https://www.pinterest.fr/John Doe/')
        self.link.network = 'L'
        self.assertEqual(self.link.url, 'https://www.linkedin.com/in/John Doe')
        self.link.network = 'Te'
        self.assertEqual(self.link.url, 'https://t.me/John Doe')
        self.link.network = 'R'
        self.assertEqual(self.link.url, 'https://www.reddit.com/user/John Doe')
        self.link.network = 'F'


class TestFriendship(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.password_creator = User.objects.make_random_password()
        cls.creator = User.objects.create_user(
            username='John Doe',
            email='John@doe.com',
            password=cls.password_creator
        )
        cls.password_friend = User.objects.make_random_password()
        cls.friend = User.objects.create_user(
            username='Bill Doe',
            email='bill@doe.com',
            password=cls.password_friend
        )
        cls.friendship = Friendship.objects.create(
            creator=cls.creator,
            friend=cls.friend,
        )

    @tag('fast')
    def test_str_method(self):
        self.assertEqual(str(self.friendship), self.creator.username + ' ❤️ ' + self.friend.username)

    @tag('fast')
    def test_accept(self):
        self.assertFalse(self.friendship.validate)
        self.friendship.accept()
        self.assertTrue(self.friendship.validate)
