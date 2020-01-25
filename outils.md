Glossaire de ce qui est utilisé pour le project.

## Git

Git est un système de gestion de controle très populaire.

Les principales commandes sont:
```shell script
git clone ssh://git@github.com:USERNAME/REPOSITORY.git # Clone le repo REPOSITORY de USERNAME avec ssh

git add fichier1 fichier2 # Ajouté fichier1 et fichier2 à git status
git add .  # Ajouté tous le répertoire à git status
git status # L'etat du repo, les fichiers ajouté pour le prochain commit, ceux modifier, ...
git rm --cached -rf fichier1 # Retirer fichier1 de git status
git rm --cached -rf . # Tous retirer de git status
git commit # Commiter une modification
git commit --amend # Editer le dernier commit

git branch # Voir toutes les branchs
git branch nom_de_la_branche # Créer la branch nom_de_la_branche
git checkout nom_de_la_branche # Aller sur la branch nom_de_la_branche
git checkout -b nom_de_la_branche # Aller sur la branch nom_de_la_branche et la créer si elle n'existe pas
git branch -d nom_de_la_branche # Supprimer nom_de_la_branche

git pull # Mettre à jour le repo depuis github et en mergeants les changements (à eviter pour un historique clair)
git pull --rebase # Mettre à jour le repo depuis github et en rebasant les changements

git merge nom_de_la_branche # Merge la branche nom_de_la_branche dans la branch actuel
git rebase nom_de_la_branche # Rebase la branche nom_de_la_branche dans la branch actuel

git push origin nom_de_la_branche # Envoit de toutes les modifications de toutes la branche nom_de_la_branche vers github
git push --all origin # Envoit de toutes les modifications de toutes les branches vers github
```

### .gitignore

Fichier de configuration de git. Tous les fichiers dans .gitingore ne serons pas
 ajouter à ```git status``` lors d'un ```git add .```


### .gitmessage

Fichier de configuration de git. Template pour commiter sur ce repo.

### .gitconfig

Fichier de configuration de git. Toutes la configuration de git specifique à ce repo.
Peut contenir des données sensible, à ne pas commiter.

## Github

Github est le site qui héberge les repo publique et privé. Voilà quelque liens
 intersant pour améliorer la securité de son compte:

- [ssh pour les repos privés](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
- [gpg/pgp pour signer ses commits](https://help.github.com/en/github/authenticating-to-github/managing-commit-signature-verification)
- [2FA](https://help.github.com/en/github/authenticating-to-github/about-two-factor-authentication)

## Pip

Pip est l'outils pour télécharger des modules python non inclue de base.

Exemple:
```shell script
pip install request # Installation du module request
pip install -r requirements.txt # Installations des modules présent dans requirements.txt
```

Sur linux on utilise pip3 (pip est la commande pour accéder à pip pour python v2)

## Django

Django est un framework de développement web extrêmement efficace et très bien documenté.

- [site](https://www.djangoproject.com/)
- [documentation](https://docs.djangoproject.com/en/3.0/)

## Folium

Folium est un outils permetant d'afficher des données cartographique sur un site web

- [repo](https://github.com/python-visualization/folium)

## data.gov.fr

Toutes les données partagé par le gouvernement français.

- [le réseau routier](https://www.data.gouv.fr/fr/datasets/voies-reseau-routier/)

## Sphinx

Surmment l'outils pour générer des documentations le plus puissant au monde

- [](https://www.sphinx-doc.org/en/master/)