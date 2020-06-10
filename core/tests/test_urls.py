from django.test import TestCase, tag
from django.urls import reverse, resolve

from core.views import *


class TestUrls(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.index_url = reverse('core:index')
        cls.privacy_url = reverse('core:privacy')
        cls.license_url = reverse('core:license')
        cls.profile_url = reverse('core:profile', args=['user'])

    @tag('fast')
    def test_index_resolved(self):
        url = self.index_url
        self.assertEqual(resolve(url).func, index)

    @tag('fast')
    def test_privacy_resolved(self):
        url = self.privacy_url
        self.assertEqual(resolve(url).func, privacy)

    @tag('fast')
    def test_license_resolved(self):
        url = self.license_url
        self.assertEqual(resolve(url).func, license)

    @tag('fast')
    def test_profile_resolved(self):
        url = self.profile_url
        self.assertEqual(resolve(url).func.view_class, ProfileDetail)
