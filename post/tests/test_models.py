from random import randrange

from django.contrib.gis.geos import MultiLineString, LineString
from django.test import TestCase, tag

from post.models import *


class TestTravel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.password = User.objects.make_random_password()
        cls.user = User.objects.create_user(
            username='John Doe',
            email='John@doe.com',
            password=cls.password
        )
        cls.multiline = MultiLineString(
            LineString((0, 0), (1, 1)),
            LineString((1, 1), (3, 3))
        )
        cls.travel = Travel.objects.create(
            creator=cls.user,
            travel=cls.multiline
        )

    @tag('fast')
    def test_str_method(self):
        self.assertEqual(str(self.travel), str(self.travel.date) + ' ' + str(self.travel.creator))


class TestPost(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.password = User.objects.make_random_password()
        cls.user = User.objects.create_user(
            username='John Doe',
            email='John@doe.com',
            password=cls.password
        )
        cls.multiline = MultiLineString(
            LineString((0, 0), (1, 1)),
            LineString((1, 1), (3, 3))
        )
        cls.travel = Travel.objects.create(
            creator=cls.user,
            travel=cls.multiline
        )
        cls.title = 'Post #1'
        cls.post = Post.objects.create(
            creator=cls.user,
            title=cls.title,
            travel=cls.travel
        )

    @tag('fast')
    def test_str_method(self):
        self.assertEqual(
            str(self.post),
            str(self.post.creator) + ' ' + str(self.post.date) + '  ' + self.post.text[:100]
        )


class TestView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.password = User.objects.make_random_password()
        cls.user = User.objects.create_user(
            username='John Doe',
            email='John@doe.com',
            password=cls.password
        )
        cls.post = Post.objects.create(
            creator=cls.user,
            title='Post #1',
        )
        cls.view = View.objects.create(
            user=cls.user,
            post=cls.post,
            like=True,
            total=randrange(0, 5)
        )

    @tag('fast')
    def test_str_method(self):
        self.view.like = False
        self.assertEqual(
            str(self.view),
            self.user.username + ' have seen ' + str(self.view.total) + ' time ' + str(self.post) + ' and ' +
            "don't like" + ' it'
        )

        self.view.like = True
        self.assertEqual(
            str(self.view),
            self.user.username + ' have seen ' + str(self.view.total) + ' time ' + str(self.post) + ' and ' +
            'like' + ' it'
        )
