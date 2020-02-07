"""
Fichier avec des données de test pour l'agorithme de suggestion

Organisation des données:

liste_info_post = [<post>, <post>, ...]

<post>: Tuple[<post_id>, <vue>, <user_list>] Un post effectué

<post_id>: int Un identifiant numerique pour le post
<vue>: int Le nombre de foit ou l'utilisateur cible a vue le post
<user_list>: List[<user>, <user>, ...] La liste des utilisateur ayant vue le post

<user>: Dict[
    'user_id': <user_id>,
    'note': <note>,
    'like': <like>,
    'friend': <friend>,
]

<user_id>: int Un identifiant numerique pour l'utilisateur
<note>: int La note de l'utilisateur
<like>: Set[<post_id>, <post_id>, ...] L'ensemble des posts que l'utilisateur à like
<friend>: Set[<user_id>, <user_id>, ...] L'ensemble des amis de l'utilisateur

"""
from random import choice, random, randint, sample
from typing import Dict, Union, List, Tuple, Set


def get_like(
        utilisateurs: List[Dict[str, Union[int, float, Set[int]]]],
        nbr_de_post: int
) -> List[Dict[str, Union[int, float, Set[int]]]]:
    """Génère une liste de post aimé pour toutes les info d'utilisateur

    :param utilisateurs: Une liste d'info utilisateur qui n'ont rien aimé
    :type utilisateurs: List[Dict[str, Union[int, float, Set[int]]]]
    :param nbr_de_post: Le nombre de post auquel il faut réagir
    :type nbr_de_post: int
    :return: La liste d'info utilisateurs avec des post aimé
    :rtype: List[Dict[str, Union[int, float, Set[int]]]]
    """
    # On obtient la liste des post aimé pour chaque utilisateurs
    like_liste = list(range(nbr_de_post))
    for utilisateur in utilisateurs:
        generosite = random()
        nbr_de_like = round(((2 * generosite + random()) / 3) * 100)
        utilisateur['like'].update(sample(like_liste, k=nbr_de_like))

    return utilisateurs


def get_friend(
        utilisateurs: List[Dict[str, Union[int, float, Set[int]]]],
        nbr_de_tetative: int
) -> List[Dict[str, Union[int, float, Set[int]]]]:
    """Génère une liste d'amis pour toutes les info d'utilisateur

    :param utilisateurs: Une liste d'info utilisateur sans amis
    :type utilisateurs: List[Dict[str, Union[int, float, Set[int]]]]
    :param nbr_de_tetative: Le nombre de foit ou l'on tentra de faire un couple d'amis
    :type nbr_de_tetative: int
    :return: La liste d'info utilisateurs avec des amis
    :rtype: List[Dict[str, Union[int, float, Set[int]]]]
    """
    # On donne à chaque utilisateur une valeur de sociabilité, plus elle est élévé plus l'utilisateur aura d'amis
    for utilisateur in utilisateurs:
        utilisateur['sociabilite'] = random()

    # On essaye de faire des couple d'amis
    for _ in range(nbr_de_tetative):
        utilisateur_1 = choice(utilisateurs)
        utilisateur_2 = choice(utilisateurs)

        # A on obtenue le meme utilisateur ?
        if utilisateur_1 == utilisateur_2:
            continue

        # A on obtenue des utilisateurs déja amis ?
        if utilisateur_1['user_id'] in utilisateur_2['friend']:
            continue
        else:
            # On tente de faire un couple d'amis
            if (utilisateur_1['sociabilite'] + utilisateur_2['sociabilite'] + random()) / 3 >= random():
                # On fait des amis
                utilisateur_1['friend'].add(utilisateur_2['user_id'])
                utilisateur_2['friend'].add(utilisateur_1['user_id'])

                # Les 2 utilisateurs deviennent + sociable
                utilisateur_1['sociabilite'] += random() / 5
                utilisateur_2['sociabilite'] += random() / 5
            else:
                # Le couple à raté, les 2 utilisateurs on des remore est aurons + de mal à se faire des amis
                utilisateur_1['sociabilite'] -= random() / 5
                utilisateur_2['sociabilite'] -= random() / 5

    # On retire à chaque utilisateur une valeur de sociabilité, elle n'est plus utile
    for utilisateur in utilisateurs:
        del utilisateur['sociabilite']

    return utilisateurs


def generate_user(nbr_utilisateur: int, nbr_de_post: int) -> List[Dict[str, Union[int, float, Set[int]]]]:
    """Génère un nombre d'info utilisateur données

    :param nbr_utilisateur: Le nombre d'info utilisateur généré
    :type nbr_utilisateur: int
    :param nbr_de_post: Le nombre de post auquel il faut réagir
    :type nbr_de_post: int
    :return: La liste des info utilisateurs généré
    :rtype: List[Dict[str, Union[int, float, Set[int]]]]
    """
    utilisateurs = []
    for user_id in range(0, nbr_utilisateur):
        utilisateurs.append({
            'user_id': user_id,
            'note': random(),
            'like': set(),
            'friend': set()
        })

    utilisateurs = get_like(utilisateurs, nbr_de_post)
    utilisateurs = get_friend(utilisateurs, round(nbr_utilisateur * random() * 15))

    return utilisateurs


def generate_post(
        nbr_de_post: int,
        nbr_utilisateur: int
) -> List[Tuple[int, Tuple[int, Dict[str, Union[int, float, Set[int]]]]]]:
    """Génère un nombre de post données

    :param nbr_de_post: Le nombre de post à générer
    :type nbr_de_post: int
    :param nbr_utilisateur: Le nombre d'info utilisateur à généré pour réagir au post
    :type nbr_utilisateur: int
    :return: Une liste de post généré
    :rtype: List[Tuple[int, Tuple[int, Dict[str, Union[int, float, Set[int]]]]]]
    """
    # On gérère des utilisateurs
    utilisateurs = generate_user(nbr_utilisateur, nbr_de_post)

    # On génère des posts vide
    posts = []
    for post_id in range(nbr_de_post):
        posts.append((post_id, randint(0, 5), []))

    possible_like_liste = list(range(nbr_de_post))
    # On lie les utilisateurs et les posts qu'il aime + des posts qu'il n'aime pas
    for utilisateur in utilisateurs:
        # On ajoute l'utilisateur au post qu'il aime
        for post_like in utilisateur['like']:
            posts[post_like][2].append(utilisateur)

        # On obtient un nombre de post à like
        nbr_de_possible_nouveau_post = round(len(utilisateur['like']) * (randint(0, 50) / 10))

        # On verifie de ne pas ajouté plus de post que possible
        if nbr_de_possible_nouveau_post > 1000:
            nbr_de_possible_nouveau_post = 1000

        # On ajoute l'utilisateur à des posts qu'il a vue mais pas like
        for post_like in sample(possible_like_liste, k=nbr_de_possible_nouveau_post):
            posts[post_like][2].append(utilisateur)

    return posts


# Pour générerer des données décommenterr le code qui suit
#
# from pickle import dump
# nbr_de_post = 2500
# nbr_de_utilisateur = round(nbr_de_post / 5)
# data = generate_post(nbr_de_post, nbr_de_utilisateur)
#
# f = open('test_data.pkl', 'wb')
# try:
#     dump(data, f)
#     f.close()
# except:
#     f.close()
