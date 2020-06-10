from django.test import TestCase, tag

from core.load import *
from core.models import VoiesMel

"""
class TestVoiesMel(TestCase):

    @classmethod
    def setUpTestData(cls):
        run(verbose=False)
        cls.voie = VoiesMel.objects.first()

    @tag('slow')
    def test_str_is_equal_to_nom_rue(self):
        self.assertEqual(str(self.voie), self.voie.nom_rue)
"""
