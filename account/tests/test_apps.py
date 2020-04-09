from django.apps import apps
from django.test import TestCase, tag

from account.apps import AccountConfig


class TestAccountConfig(TestCase):

    @tag('fast')
    def test_apps(self):
        self.assertEqual(AccountConfig.name, apps.get_app_config('account').name)
