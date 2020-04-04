from unittest import TestCase

from django.test import tag

from ..fonction import add


class Test(TestCase):

    @tag('fast')
    def test_add(self):
        # https://docs.python.org/3/library/unittest.html#assert-methods
        # On test les parametres
        with self.assertRaises(TypeError):
            add('1', 5)

        # On test pour les int
        self.assertAlmostEqual(add(1, 1), 2)
        self.assertAlmostEqual(add(1, -2), -1)

        # On test pour les float
        self.assertAlmostEqual(add(0.1, -0.5), -0.4)
        self.assertAlmostEqual(add(-0.1, 100), 99.9)

        # On test des valeurs fause
        self.assertNotAlmostEqual(add(1, 1), 3)

        # On test la valeurs de retour
        self.assertIsInstance(add(1, 1), int)
        self.assertIsInstance(add(1, 2.0), float)
