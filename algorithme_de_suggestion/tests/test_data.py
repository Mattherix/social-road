from random import random
from unittest import TestCase

from django.test import tag

from ..data import get_like, get_friend, generate_user, generate_post


class Test(TestCase):
    def setUp(self) -> None:
        self.NBR_DE_POST = 2500
        self.NBR_UTILISATEUR = round(self.NBR_DE_POST / 5)

        # On obtient des utilisateurs sans like ou amis
        self.utilisateurs = []
        for user_id in range(0, self.NBR_UTILISATEUR):
            self.utilisateurs.append({
                'user_id': user_id,
                'note': random(),
                'like': set(),
                'friend': set()
            })

    @tag('fast')
    def test_get_like(self):
        # On ne peut pas tester les resultats car ils sont lier au hasard
        #   On va donc juste lancer la fonction et voir le temps d'execution
        get_like(self.utilisateurs, self.NBR_DE_POST)

    @tag('fast')
    def test_get_friend(self):
        # On ne peut pas tester les resultats car ils sont lier au hasard
        #   On va donc juste lancer la fonction et voir le temps d'execution
        get_friend(self.utilisateurs, round(self.NBR_UTILISATEUR * random() * 15))

    @tag('fast')
    def test_generate_user(self):
        # On ne peut pas tester les resultats car ils sont lier au hasard
        #   On va donc juste lancer la fonction et voir le temps d'execution
        generate_user(self.NBR_UTILISATEUR, self.NBR_DE_POST)

    @tag('fast')
    def test_generate_post(self):
        # On ne peut pas tester les resultats car ils sont lier au hasard
        #   On va donc juste lancer la fonction et voir le temps d'execution
        generate_post(self.NBR_DE_POST, self.NBR_UTILISATEUR)
