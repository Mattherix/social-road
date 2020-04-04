from django.test import TestCase, tag
from django.urls import reverse

from account.models import User
from social_road.decorator import login_logout


class TestView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.register_url = reverse('account:register')
        cls.login_url = reverse('account:login')
        cls.logout_url = reverse('account:logout')
        cls.edit_url = reverse('account:edit')
        cls.friends_url = reverse('account:friends')
        cls.notifications_url = reverse('account:notifications')

        cls.password = User.objects.make_random_password()
        cls.user = User.objects.create_user(
            username='John Doe',
            email='John@doe.com',
            password=cls.password
        )

    @tag('fast')
    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')

    @tag('fast')
    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    @tag('fast')
    def test_logout_not_logged_GET(self):
        response = self.client.get(self.logout_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    @tag('fast')
    @login_logout
    def test_logout_logged_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEqual(response.status_code, 200)

    @tag('fast')
    def test_edit_not_logged_GET(self):
        response = self.client.get(self.edit_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    @tag('fast')
    @login_logout
    def test_edit_logged_GET(self):
        response = self.client.get(self.edit_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/edit.html')

    @tag('fast')
    def test_friends_not_logged_GET(self):
        response = self.client.get(self.friends_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    @tag('fast')
    @login_logout
    def test_friends_logged_GET(self):
        response = self.client.get(self.friends_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/friends.html')

    @tag('fast')
    def test_notifications_not_logged_GET(self):
        response = self.client.get(self.notifications_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    @tag('fast')
    @login_logout
    def test_notifications_logged_GET(self):
        response = self.client.get(self.notifications_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/notifications.html')
