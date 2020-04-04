from django.test import TestCase, tag
from django.urls import reverse

from account.models import User
from post.models import Post
from social_road.decorator import login_logout


class TestViews(TestCase):

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
    def test_new_post_url_not_logged_GET(self):
        response = self.client.get(self.new_post_url, follow=True)

        self.assertEqual(response.status_code, 200)

    @tag('fast')
    @login_logout
    def test_new_post_url_logged_GET(self):
        response = self.client.get(self.new_post_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/new_post.html')

    @tag('fast')
    def test_posts_url_not_logged_GET(self):
        response = self.client.get(self.posts_url, follow=True)

        self.assertEqual(response.status_code, 200)

    @tag('fast')
    @login_logout
    def test_posts_url_logged_GET(self):
        response = self.client.get(self.posts_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/posts.html')

    @tag('fast')
    def test_post_url_not_logged_GET(self):
        response = self.client.get(self.post_url, follow=True)

        self.assertEqual(response.status_code, 200)

    @tag('fast')
    @login_logout
    def test_post_url_logged_GET(self):
        response = self.client.get(self.post_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/post.html')
