from django.test import TestCase, tag

from django.apps import apps
from post.apps import PostConfig


class TestPostConfig(TestCase):

    @tag('fast')
    def test_apps(self):
        self.assertEqual(PostConfig.name, apps.get_app_config('post').name)
