"""
Ce fichier contient toutes les fonction lier à l'algorithme de suggestion du contenue.

Fonctionnement
==============

On va noté chaque post afin de renvoyer un classement.

La note d'un post est déterminé ainsi:

note = probabilité que l'utilisateur aime le post * (1/sqrt(vue + 1))

Avec:

    * vue: le nombre de foix ou l'utilisateur a vue le post

Les nouveaux post (moins de 20 vue) sont noté dans un classsement séparé.

On revoie une liste contenant le nombre d'éléments demandé dont un pourcentage demandé de nouveau

Calcule de la probabilité que l'utilisateur aime le post
--------------------------------------------------------

Chaque utilisateurs possède des labels qu'il récolte au cours de sa navigation sur le site.

Les labels possible sont:

    * Les Labels lier au like
    * Les Labels d'amitié: les amis de l'utilisateurs

Chaque post est vue par un certain nombre d'utilisateur.

On peut ainsi obtenir un tableau:

| user_id | like | label 1 | label 2 |...|
|--|--|--|--|--|
| 1 | True | True | False | ... |
| 2 | False | False | True | ... |
| 5 | True | True | False | ... |
| 10 | True | True | True | ... |
| ... |

avec:

    * user_id: un identifiant pour chaque utilisateur
    * like: l'utilisateur a t'il like ?
    * label x: l'utilisateur a il le label x

on veux calculer la probabilité que l'on aime le post sachant l'experience de l'utilisateur(tous ses label) soit:

P(aime le post A|expérience user 1)

[le théorème de bayes](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Bayes)
 nous dit que:

P(aime le post A|expérience user 1) = (antérieur * vraisemblance) / évidence

avec:

    * antérieur = P(aime le post A)
    * vraisemblance = p(label 1|aime le post A)*p(label 2|aime le post A)*...
    * évidence = p(label 1)*p(label 2)*...

en supposant que les label sont indépendant

On obtient alors la probabilité que l'utilisateur aime le post.

Plus d'info:
-----------

([Youtube](https://youtu.be/CPqOCI0ahss))

([Wikipédia](https://fr.wikipedia.org/wiki/Classification_na%C3%AFve_bay%C3%A9sienne))


"""
from typing import List, Dict, Union, Tuple, Set
from math import sqrt
from fractions import Fraction


def transforme_post(
        post: Tuple[int, Tuple[int, Dict[str, Union[int, bool, Set[int]]]]]
) -> Tuple[List[Tuple[str, int]], List[List[bool]]]:
    """Transforme un post en un tableau contenant les utilisateurs selon leurs labels

    Transforme un post en un tableau, le premier élément de chaque ligne et l'user_id,
    les significations des collones sont données dans un dictionnaire s'organnisant ainsi:
    {
        'like': {post_id: index_collone, ...},
        'friend': {post_id: index_collone, ...}
    }

    :param post: Les informations d'un post
    :type post: Tuple[int, Tuple[int, Dict[str, Union[int, bool, Set[int]]]]]
    :return: Un tuple contenant le dictionnaire faissant le lien post_id -> colone et le tableau
    :rtype: Tuple[Dict[str, Dict[int, int]], List[List[bool]]]

    (Une explication plus precise des paramètre sont dans le fichier data du module)
    """
    # On crée une copie de la liste afin d'éviter les effets de bord
    user_liste = list(post[2])

    # On cherche tous les label lier au post et on les inclues à la première liste du tableau
    liste_label = []
    for user in user_liste:
        for like in user['like']:
            # On donne un numero de colone si ce label n'en a pas
            if ('like', like) not in liste_label:
                liste_label.append(('like', like))
        for friend in user['friend']:
            # Même chose mais pour les amis
            if ('friend', friend) not in liste_label:
                liste_label.append(('friend', friend))

    # On crée le tabeau en iterant dans la liste des utilisateurs
    tableau = []
    for user in user_liste:
        ligne = []
        # Pour chaque label possible ...
        for label in liste_label:
            # On ajoute True si l'utilisateur l'a et False si il ne l'a pas
            if label[1] in user[label[0]]:
                ligne.append(True)
            else:
                ligne.append(False)
        tableau.append(ligne)

    return liste_label, tableau


def note_post(
        post: Tuple[int, Tuple[int, Dict[str, Union[int, bool, Set[int]]]]],
        user: Dict[str, Union[int, float, Set[int]]]
) -> Fraction:
    """Note un post par rapport a l'utilisateur

    Cette fonction utilise l'equation de bayes afin de renvoyer
    la probabilité que l'utilisateur like sachant l'experience
    de l'utilisateur cible

    :param post: Les informations d'un post
    :type post: Tuple[int, Tuple[int, Dict[str, Union[int, bool, Set[int]]]]]
    :param user: Les informations de l'utilisateur cible
    :type user: Dict[str, Union[int, bool, Set[int]]]
    :return: La probabilité que l'utilisateur like sachant sont experiences
    :rtype: Fraction

    (Une explication plus precise des paramètre sont dans le fichier data du module)
    """
    # On trasforme la liste les utilisateurs pour obtenir un tableau des données
    liste_label, tableau = transforme_post(post)

    # On instancie des variables pour clarifier le code
    post_id = post[0]

    # Pour chaque label on compte le nombre de positif et de négatif
    nbr_de_label = {
        'like': {
            True: {},
            False: {}
        },
        'friend': {
            True: {},
            False: {}
        }
    }
    for numero_de_la_colone, label in enumerate(liste_label):
        for utilisateur in tableau:
            if label[1] not in nbr_de_label[label[0]][True]:
                nbr_de_label[label[0]][True][label[1]] = 0
            if label[1] not in nbr_de_label[label[0]][False]:
                nbr_de_label[label[0]][False][label[1]] = 0

            if utilisateur[numero_de_la_colone]:
                nbr_de_label[label[0]][True][label[1]] += 1
            else:
                nbr_de_label[label[0]][False][label[1]] += 1

    # On cherche les paramètre de l'équation de bayes pour l'utilisateur
    # On calcule la vraisemblance
    vraisemblance = 1
    for type_du_label in nbr_de_label:
        for label in liste_label:
            if label[0] != type_du_label:
                continue

            if label[1] in user[type_du_label]:
                condition = True
            else:
                condition = False

            # nbr_de_foix_ou le label apparait / nbr_de_like
            vraisemblance *= Fraction(
                nbr_de_label[type_du_label][condition][label[1]],
                nbr_de_label[type_du_label][condition][label[1]] + nbr_de_label[type_du_label][not condition][label[1]]
            )

    # On calcule l'évidence
    nbr_utilisateur = len(tableau)
    evidence = 1
    for type_du_label in nbr_de_label:
        for label in liste_label:
            if label[0] != type_du_label:
                continue

            if label[1] in user[type_du_label]:
                condition = True
            else:
                condition = False

            #  nbr_de_foix_ou_le_label_apparait / nbr_utilisateur
            evidence *= Fraction(nbr_de_label[type_du_label][condition][label[1]], nbr_utilisateur)

    # On calcule l'anterieur
    anterieur = Fraction(nbr_de_label['like'][True][post_id], nbr_utilisateur)

    # On applique le théorème de bayes
    note = Fraction(anterieur * vraisemblance, evidence)
    return note


def suggestion(
        liste_info_post: List[Tuple[int, Tuple[int, Dict[str, Union[int, float, Set[int]]]]]],
        user: Dict[str, Union[int, float, Set[int]]],
        liste_info_nouveau_post: List[Tuple[int, Tuple[int, Dict[str, Union[int, float, Set[int]]]]]] = None,
        nbr_de_reponse: int = None,
        proportion_de_nouveaute: float = 0.2
) -> List[int]:
    """Renvoie les contenues les plus pertinent pour un utilisateur

    Cette fonction utilise l'equation de bayes afin de suggerer le post le plus
    pertinent. Des explications sur sont fonctionnement se trouve dans l'aide principale
    du module. Une proportion de nouveauté (par rapport à la platforme) peux être
    mis en avant automatiquement parmis les réponses.

    :param liste_info_post: La liste des information sur le post
    :type liste_info_post: List[Tuple[int, Tuple[int, Dict[str, Union[int, float, Set[int]]]]]]
    :param user: Les informations de l'utilisateur cible
    :type user: Dict[str, Union[int, float, Set[int]]]
    :param liste_info_nouveau_post: La liste des informations sur les nouveaux posts
    :type liste_info_nouveau_post: List[Tuple[int, Tuple[int, Dict[str, Union[int, float, Set[int]]]]]]
    :param nbr_de_reponse: Le nombre de réponse attendue
    :type nbr_de_reponse: int
    :param proportion_de_nouveaute: La proportion de nouveauté mis en avant (de 0 à 1)
    :type proportion_de_nouveaute: float
    :return: Une liste d'id des posts par ordre de préference
    :rtype: List[int]

    (Une explication plus precise des paramètre sont dans le fichier data du module)
    """
    # A t'on des nouveaux posts ?
    if liste_info_nouveau_post:
        # On obtenient un classement des nouveaux posts
        classement_nouveau = suggestion(liste_info_nouveau_post, user)
        del liste_info_nouveau_post

        # On obtenient un classement des anciens posts
        classement_ancien = suggestion(liste_info_post, user)
        del liste_info_post

        # On obtient un nombre de réponse si l'on en a pas
        if not nbr_de_reponse:
            nbr_de_reponse = len(classement_nouveau) + len(classement_ancien) + 1

        # On mélange les 2 classements
        classement = []
        index_ancien = 0
        index_nouveau = 0
        proportion = proportion_de_nouveaute
        # A chaque tour on ajoute la proportion demandé à 'proportion'
        #   quand 'proportion' est à 1  ou pluson ajoute un nouveau post
        #   et on met 'proportion' à:
        #   'proportion_de_nouveaute' + 'proposition' - 1
        for _ in range(nbr_de_reponse - 1):
            if proportion >= 1:
                classement.append(classement_ancien[index_ancien])
                index_ancien += 1
                proportion = (proportion - 1) + proportion_de_nouveaute
            else:
                classement.append(classement_nouveau[index_nouveau])
                index_nouveau += 1
                proportion += proportion_de_nouveaute

        return classement
    else:
        # On note chaque posts
        note_des_posts: List[Tuple[int, float]] = []  # [(post_id, note), ...]
        for post in liste_info_post:
            note_des_posts.append(
                (
                    post[0],
                    note_post(post, user) * (1 / sqrt(post[1] + 1))
                )
            )
        del liste_info_post

        # On trie les résultats selon les notes
        note_des_posts.sort(key=lambda post_id_et_note: post_id_et_note[1])

        # On retire les notes
        classement = [post_id_et_note[0] for post_id_et_note in note_des_posts]

        # Y a il un nombre de réponse limite ?
        if nbr_de_reponse:
            # Oui
            return classement[0:nbr_de_reponse]
        else:
            # Non
            return classement


from pickle import load

f = open('tests/algorithme_de_suggestion.pkl', 'rb')
try:
    data = load(f)
finally:
    f.close()

print(suggestion(data, data[1565][2][15], nbr_de_reponse=10))

"""

    # On instancie des variables pour clarifier le code
    post_id = post[0]
    # On crée une copie de la liste afin d'éviter les effet de bord
    user_liste = list(post[2])
    nbr_utilisateur = len(user_liste)

    # On retire les utilisateurs qui n'ont pas like le post
    user_liste = [user for user in user_liste if post_id in user['like']]

    # On dénombre tous les labels liés à l'experience de l'utilisateur et aux utilisateurs qui on like le post
    label_like = {
        'like': {},
        'friend': {}
    }
    label = {
        'like': {},
        'friend': {}
    }
    for utilisateur in user_liste:
        for like in utilisateur['like']:
            if like in user['like']:
                try:
                    label_like['like'][like] += 1
                except KeyError:
                    label_like['like'][like] = 1
            try:
                label['like'][like] += 1
            except KeyError:
                label['like'][like] = 1
        for friend in utilisateur['friend']:
            if friend in user['friend']:
                try:
                    label_like['friend'][friend] += 1
                except KeyError:
                    label_like['friend'][friend] = 1
            try:
                label['like'][like] += 1
            except KeyError:
                label['like'][like] = 1

    # On obtient les termes de l'équation de bayes
    # anterieur -> P(aime le post) = nbr_de_like / nbr_utilisateur
    nbr_de_like = label['like'][post_id]
    anterieur = Decimal(nbr_de_like) / Decimal(nbr_utilisateur)

    # vraisemblance -> P(label 1|aime le post)*p(label 2|aime le post)*...
    #   avec P(label|aime le post) = P(l & A)/P(A) =
    #   (nbr_de_personne_ayant_like_avec_le_label/nbr_utilisateur)/(nbr_de_like / nbr_utilisateur)
    #   = nbr_de_personne_ayant_like_avec_le_label / nbr_de_like
    #   On ne compte que les labels dans l'experience de l'utilisateur
    # évidence -> p(label 1)*p(label 2)*...
    #   avec P(label) = nbr_de_personne_avec_le_label / nbr_utilisateur
    vraisemblance = 1
    # On obtient les valeurs des labels lié à l'utilisateur
    liste_des_labels_qui_ont_like = list(label_like['like'].values()) + list(label_like['friend'].values())
    for nbr_de_personne_avec_le_label_qui_on_like in liste_des_labels_qui_ont_like:
        # Pour chaque label on obtient la vraisemblance et l'évidence
        vraisemblance *= (Decimal(nbr_de_personne_avec_le_label_qui_on_like) / Decimal(nbr_de_like))

    evidence = 1
    liste_des_labels = list(label['like'].values()) + list(label['friend'].values())
    for nbr_de_personne_avec_le_label in liste_des_labels:
        evidence *= (Decimal(nbr_de_personne_avec_le_label) / Decimal(nbr_utilisateur))

    # On applique le théorème de bayes
    note = (anterieur * vraisemblance) / evidence
    return note
"""
