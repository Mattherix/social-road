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
from decimal import Decimal, getcontext
from typing import List, Dict, Union, Tuple, Set
from math import sqrt
from multiprocessing import Pool

getcontext().prec = 10  # Precision des calcules


def note_post(
        post: Tuple[int, Tuple[int, Dict[str, Union[int, bool, Set[int]]]]],
        user: Dict[str, Union[int, float, Set[int]]]
) -> Decimal:
    """Note un post par rapport a l'utilisateur

    Cette fonction utilise l'equation de bayes afin de renvoyer
    la probabilité que l'utilisateur like sachant l'experience
    de l'utilisateur cible
    Attention, afin de ne pas avoir de probablité égale à 0 le calcule est biaisé.

    :param post: Les informations d'un post
    :type post: Tuple[int, Tuple[int, Dict[str, Union[int, bool, Set[int]]]]]
    :param user: Les informations de l'utilisateur cible
    :type user: Dict[str, Union[int, bool, Set[int]]]
    :return: La probabilité biaisé que l'utilisateur like sachant sont experiences
    :rtype: Decimal

    (Une explication plus precise des paramètre sont dans le fichier data du module)
    """
    # On crée une copie de la liste afin d'éviter les effets de bord
    user_liste = list(post[2])

    # On instancie des variables pour clarifier le code
    post_id = post[0]
    nbr_utilisateur = len(user_liste)

    # On cherche les labels liés au utilisateurs lier au post
    labels = {
        'like': set(),
        'friend': set()
    }
    for utilisateur in user_liste:
        for type_de_label in ['like', 'friend']:
            for label in utilisateur[type_de_label]:
                labels[type_de_label].add(label)

    # On dénombre la nombre de labels
    # nbr_de_label[type_de_label][condition][aime]
    nbr_de_label = {
        'like': {
            True: {True: {}, False: {}},
            False: {True: {}, False: {}}
        },
        'friend': {
            True: {True: {}, False: {}},
            False: {True: {}, False: {}}
        }
    }
    for utilisateur in user_liste:
        if post_id in utilisateur['like']:
            aime = True
        else:
            aime = False
        for type_de_label, dict_type_de_label in nbr_de_label.items():
            for label in labels[type_de_label]:
                # On ajoute le label s'il n'est pas dans le dictionnaire
                if label not in dict_type_de_label[True][True]:
                    dict_type_de_label[True][True][label] = 0
                if label not in dict_type_de_label[False][True]:
                    dict_type_de_label[False][True][label] = 0
                if label not in dict_type_de_label[True][False]:
                    dict_type_de_label[True][False][label] = 0
                if label not in dict_type_de_label[False][False]:
                    dict_type_de_label[False][False][label] = 0

                # On incremente le nombre d'utilisateur avec/sans le label si l'utilisateur l'a/ne l'a pas
                if label in utilisateur[type_de_label]:
                    dict_type_de_label[True][aime][label] += 1
                else:
                    dict_type_de_label[False][aime][label] += 1

    # On cherche les paramètres de l'équation de bayes pour l'utilisateur
    # On calcule la vraisemblance et l'évidence
    vraisemblance = 1
    evidence = 1
    for type_de_label in ['like', 'friend']:
        for label in labels[type_de_label]:
            # On regarde si l'utilisateur a le label ou pas
            if label in user[type_de_label]:
                condition = True
            else:
                condition = False

            nbr_total_du_label = \
                Decimal(nbr_de_label[type_de_label][condition][True][label]) + \
                Decimal(nbr_de_label[type_de_label][condition][False][label])

            nbr_de_foix_ou_le_label_apparait = Decimal(nbr_de_label[type_de_label][condition][True][label])
            if nbr_de_foix_ou_le_label_apparait == 0:
                # On evite ainsi de mettre la vraisemblance à 0, néamoins la probabilité est biaisé
                nbr_de_foix_ou_le_label_apparait = 1

            # Vraisemblance: nbr_de_foix_ou_le_label_apparait_sachant_que_l'on_aime / nbr_de_label_sachant_que_l'on_aime
            vraisemblance *= \
                Decimal(nbr_de_foix_ou_le_label_apparait) / Decimal(nbr_total_du_label)

            # Evidence: nbr_de_foix_ou_le_label_apparait / nbr_utilisateur
            evidence *= Decimal(nbr_total_du_label) / Decimal(nbr_utilisateur)

    # On calcule l'anterieur
    anterieur = \
        Decimal(nbr_de_label['like'][True][True][post_id] +
                nbr_de_label['like'][True][False][post_id]) / Decimal(nbr_utilisateur)

    # On applique le théorème de bayes
    note = anterieur * vraisemblance / evidence
    return note


def notation_post(
        post: Tuple[int, Tuple[int, Dict[str, Union[int, bool, Set[int]]]]],
        user: Dict[str, Union[int, float, Set[int]]]
) -> Tuple[int, Decimal]:
    """Donne la notation finale d'un post sois probabilité que l'utilisateur aime le post * (1/sqrt(vue + 1))

    :param post: Les informations d'un post
    :type post: Tuple[int, Tuple[int, Dict[str, Union[int, bool, Set[int]]]]]
    :param user: Les informations de l'utilisateur cible
    :type user: Dict[str, Union[int, bool, Set[int]]]
    :return: Le post_id et la note du post pour l'utilisateur
    :rtype: Tuple[int, Decimal]
    """
    return post[0], note_post(post, user) * Decimal(1 / sqrt(post[1] + 1))


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

        # On mélange les 2 classements
        classement = []
        proportion = float(proportion_de_nouveaute)
        # A chaque tour on ajoute la proportion demandé à 'proportion'
        #   quand 'proportion' est à 1  ou pluson ajoute un nouveau post
        #   et on met 'proportion' à:
        #   'proportion_de_nouveaute' + 'proposition' - 1
        while len(classement_ancien) + len(classement_nouveau) != 0:
            if proportion >= 1 and len(classement_nouveau) != 0:
                classement.append(classement_nouveau.pop(0))
                proportion = (proportion - 1) + proportion_de_nouveaute
            else:
                classement.append(classement_ancien.pop(0))
                proportion += proportion_de_nouveaute

        # Y a il un nombre de réponse limite ?
        if nbr_de_reponse:
            # Oui
            return classement[0:nbr_de_reponse]
        else:
            # Non
            return classement
    else:
        # On note chaque posts
        # On lance plusieurs processus pour accelérer les calcules
        user_liste = [user for _ in range(len(liste_info_post))]
        with Pool() as pool:
            note_des_posts = pool.starmap(
                notation_post,
                zip(liste_info_post, user_liste)
            )  # [(post_id, note), ...]

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
