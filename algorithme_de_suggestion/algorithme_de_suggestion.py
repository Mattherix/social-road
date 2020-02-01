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
