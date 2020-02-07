"""
Ce fichier contient toutes les fonction lier à l'algorithme de suggestion du contenue.

Fonctionnement
--------------

On va noté chaque post afin de renvoyer un classement.

La note d'un post est déterminé ainsi:

note = probabilité que l'utilisateur aime le post * (1/sqrt(vue + 1))

Avec:

    * vue: le nombre de foix ou l'utilisateur a vue le post

Les nouveaux post (moins de 20 vue) sont noté dans un classsement séparé.

On revoie une liste contenant le nombre d'éléments demandé dont un pourcentage demandé de nouveau

Calcule de la probabilité que l'utilisateur aime le post
========================================================

Chaque utilisateurs possède des labels qu'il récolte au cours de sa navigation sur le site.

Les labels possible sont:

    * Les Labels lier au like
    * Les Labels d'amitié: les amis de l'utilisateurs
    * (pas sur d'être mis)Label groupe: les groupes ou l'utilisateur est

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
([+ info](https://fr.wikipedia.org/wiki/Classification_na%C3%AFve_bay%C3%A9sienne#Mod%C3%A8le_bay%C3%A9sien_na%C3%AFf))

On obtient alors la probabilité que l'utilisateur aime le post.


"""
from typing import List, Dict, Union, Tuple, Set

import typeguard


@typeguard.typechecked
def note_post(
        post: Tuple[int, Tuple[int, Dict[str, Union[int, bool, Set[int]]]]],
        user: Dict[str, Union[int, float, Set[int]]]
) -> float:
    """Note un post par rapport a l'utilisateur

    Cette fonction utilise l'equation de bayes afin de renvoyer
    la probabilité que l'utilisateur like sachant l'experience
    de l'utilisateur cible

    :param post: Les informations d'un post
    :type post: Tuple[int, Tuple[int, Dict[str, Union[int, bool, Set[int]]]]]
    :param user: Les informations de l'utilisateur cible
    :type user: Dict[str, Union[int, bool, Set[int]]]
    :return: La probabilité que l'utilisateur like sachant sont experiences
    :rtype: float

    (Une explication plus precise des paramètre sont dans le fichier data du module)
    """


@typeguard.typechecked
def suggestion(
        liste_info_post: List[Tuple[int, Tuple[int, Dict[str, Union[int, float, Set[int]]]]]],
        user: Dict[str, Union[int, float, Set[int]]],
        list_info_nouveau_post: List[Tuple[int, Tuple[int, Dict[str, Union[int, float, Set[int]]]]]] = None,
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
    :param list_info_nouveau_post: La liste des informations sur les nouveaux posts
    :type list_info_nouveau_post: List[Tuple[int, Tuple[int, Dict[str, Union[int, float, Set[int]]]]]]
    :param nbr_de_reponse: Le nombre de réponse attendue
    :type nbr_de_reponse: int
    :param proportion_de_nouveaute: La proportion de nouveauté mis en avant (de 0 à 1)
    :type proportion_de_nouveaute: float
    :return: Une liste d'id des posts par ordre de préference
    :rtype: List[int]

    (Une explication plus precise des paramètre sont dans le fichier data du module)
    """
