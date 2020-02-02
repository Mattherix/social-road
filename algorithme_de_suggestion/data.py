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
    'like_list': <like_list>,
    'friend': <friend>,
]

<user_id>: int Un identifiant numerique pour l'utilisateur
<note>: int La note de l'utilisateur
<like>: bool A True si l'utilisateur a like sinon False
<like_list>: List[<post_id>, <post_id>, ...] La liste des posts que l'utilisateur à like
<friend>: List[<user_id>, <user_id>, ...] La liste des amis de l'utilisateur

"""
from random import choice, random, randint
from typing import Dict, Union, List, Tuple


def get_like_liste(nbr_de_post: int) -> List[int]:
    """Génère une liste de post aimé pour une info d'utilisateur

    :param nbr_de_post: Le nombre de post auquel il faut réagir
    :type nbr_de_post: int
    :return: Une liste de post id aimé
    :rtype: List[int]
    """
    # On obtient la liste des posts like
    like_liste = []
    generosite = random()  # Plus ce nombre est élévé plus on like de post
    for post_id in range(nbr_de_post):
        if (2 * generosite + random()) / 3 >= 2 * random():
            like_liste.append(post_id)

    return like_liste


def get_friend(
        utilisateurs: List[Dict[str, Union[int, float, List[int]]]],
        nbr_de_tetative: int
) -> List[Dict[str, Union[int, float, List[int]]]]:
    """Génère une liste d'amis pour toutes les info d'utilisateur

    :param utilisateurs: Une liste d'info utilisateur sans amis
    :type utilisateurs: List[Dict[str, Union[int, float, List[int]]]]
    :param nbr_de_tetative: Le nombre de foit ou l'on tentra de faire un couple d'amis
    :type nbr_de_tetative: int
    :return: Une list de user
    :rtype: List[Dict[str, Union[int, float, List[int]]]]
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
                utilisateur_1['friend'].append(utilisateur_2['user_id'])
                utilisateur_2['friend'].append(utilisateur_1['user_id'])

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


def generate_user(nbr_utilisateur: int, nbr_de_post: int) -> List[Dict[str, Union[int, float, List[int]]]]:
    """Génère un nombre d'info utilisateur données

    :param nbr_utilisateur: Le nombre d'info utilisateur généré
    :type nbr_utilisateur: int
    :param nbr_de_post: Le nombre de post auquel il faut réagir
    :type nbr_de_post: int
    :return: La liste des info utilisateurs généré
    :rtype: List[Dict[str, Union[int, float, List[int]]]]
    """
    utilisateurs = []
    for user_id in range(0, nbr_utilisateur):
        utilisateurs.append({
            'user_id': user_id,
            'note': random(),
            'like_list': get_like_liste(nbr_de_post),
            'friend': []
        })

    utilisateurs = get_friend(utilisateurs, round(nbr_utilisateur * random() * 15))

    return utilisateurs


def generate_post(
        nbr_de_post: int,
        nbr_utilisateur: int
) -> List[Tuple[int, Tuple[int, Dict[str, Union[int, float, List[int]]]]]]:
    """Génère un nombre de post données

    :param nbr_de_post: Le nombre de post à générer
    :type nbr_de_post: int
    :param nbr_utilisateur: Le nombre d'info utilisateur à généré pour réagir au post
    :type nbr_utilisateur: int
    :return: Une liste de post généré
    :rtype: List[Tuple[int, Tuple[int, Dict[str, Union[int, float, List[int]]]]]]
    """
    # On génère des posts vide
    posts = []
    for post_id in range(nbr_de_post):
        posts.append((post_id, randint(0, 5), []))

    # On gérère des utilisateurs
    utilisateurs = generate_user(nbr_utilisateur, nbr_de_post)

    # On lie les utilisateurs et les posts qu'il aime
    for utilisateur in utilisateurs:
        for post_like in utilisateur['like_list']:
            posts[post_like][2].append(utilisateur)

    # On fait voir de post à des personnes qui ne le likerons pas
    for post in posts:
        # On tente de faire voir le post à un nombre d'utilisateur dépendant du nombre d'utilisateur ayant like
        for _ in range(round(len(post[2]) * random() * 2)):
            utilisateur = choice(utilisateurs)

            # A on obtenue un utilisateur qui a like ?
            if utilisateur in post[2]:
                continue
            else:
                # L'utilisateur à vue le post
                post[2].append(utilisateur)

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
