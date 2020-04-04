from django.test import TestCase, tag

from django.apps import apps
from core.apps import CoreConfig


class TestCoreConfig(TestCase):

    @tag('fast')
    def test_apps(self):
        self.assertEqual(CoreConfig.name, apps.get_app_config('core').name)
