from django.test import TestCase, tag
from django.urls import reverse, resolve

from account.views import *


class TestUrls(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.register_url = reverse('account:register')
        cls.login_url = reverse('account:login')
        cls.logout_url = reverse('account:logout')
        cls.edit_url = reverse('account:edit')
        cls.friends_url = reverse('account:friends')
        cls.notifications_url = reverse('account:notifications')

    @tag('fast')
    def test_register_resolved(self):
        url = self.register_url
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    @tag('fast')
    def test_login_resolved(self):
        url = self.login_url
        self.assertEqual(resolve(url).func, login_view)

    @tag('fast')
    def test_logout_resolved(self):
        url = self.logout_url
        self.assertEqual(resolve(url).func, logout_view)

    @tag('fast')
    def test_edit_resolved(self):
        url = self.edit_url
        self.assertEqual(resolve(url).func, edit_view)

    @tag('fast')
    def test_friends_resolved(self):
        url = self.friends_url
        self.assertEqual(resolve(url).func.view_class, FriendList)

    @tag('fast')
    def test_notifications_resolved(self):
        url = self.notifications_url
        self.assertEqual(resolve(url).func.view_class, NotificationList)
