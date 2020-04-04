from django.test import TestCase, tag
from django.urls import reverse

from account.models import User
from social_road.decorator import login_logout


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.index_url = reverse('core:index')
        cls.privacy_url = reverse('core:privacy')
        cls.license_url = reverse('core:license')
        
        cls.password = User.objects.make_random_password()
        cls.user = User.objects.create_user(
            username='John Doe',
            email='John@doe.com',
            password=cls.password
        )
        slug = cls.user.slug
        cls.profile_url = reverse('core:profile', args=[slug])

    @tag('fast')
    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    @tag('fast')
    def test_privacy_GET(self):
        response = self.client.get(self.privacy_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacy.html')

    @tag('fast')
    def test_license_GET(self):
        response = self.client.get(self.license_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'license.html')

    @tag('fast')
    def test_profile_not_logged_GET(self):
        response = self.client.get(self.profile_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    @tag('fast')
    @login_logout
    def test_profile_logged_GET(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(self.profile_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
