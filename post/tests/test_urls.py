from django.test import TestCase, tag
from django.urls import reverse, resolve

from post.views import *
from account.models import User


class TestUrls(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.new_post_url = reverse('post:new_post')
        cls.posts_url = reverse('post:posts')

        cls.password = User.objects.make_random_password()
        cls.user = User.objects.create_user(
            username='John Doe',
            email='John@doe.com',
            password=cls.password
        )
        cls.post = Post.objects.create(
            creator=cls.user,
            title='Post #1'
        )
        cls.post_url = reverse('post:post', args=[cls.post.pk])

    @tag('fast')
    def test_new_post_resolved(self):
        url = self.new_post_url
        self.assertEqual(resolve(url).func, new_post)

    @tag('fast')
    def test_posts_resolved(self):
        url = self.posts_url
        self.assertEqual(resolve(url).func.view_class, PostList)

    @tag('fast')
    def test_post_resolved(self):
        url = self.post_url
        self.assertEqual(resolve(url).func.view_class, PostDetail)
