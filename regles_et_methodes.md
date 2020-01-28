Pour mener à bien un projet il faut de la méthode et des règles.

Volà l'approche à avoir pour les princicipals actions autours du projet

## Github project

A prendre en compte pour tous les actions possibles.

A chaque foit que vous agisser créer un carte où bouger en une.

Les cartes peuvent bouger entre

- To Do(à faire),
- In progress (vous agissez),
- Review in progress (Les autre developpers vous relises)
- Done (Le travail est fini)

Chaque carte est une issue.

Quand on commit on doit ajouté dans le footer du commit l'issue (cf. .gitmessage).

On doit ajouté à l'issue un lien vers notre commit

## Modification/Ajout de fonctionnalité

### Petit modification (des modifications peut importante)

Faite une issue et commit vers master, c'est peu important

### Autre modification

- Créer une issue
- Créer une branche (en local) avec un nom explicite pour la modification
- Faire autant de commit qu'il faut
- Faire un push vers le repo principal
- Creer une pull request et assigner tous les membres de la developper team
 pour que votre PR passe ils doivent tous rendre une review positif
- Anoncer votre PR sur teams
- Si votre PR est accepté votre branche sera merge dans master et fermé
- Sinon la PR sera fermé

## Commit

Pour tous les commits sur se repo.

- Codé les modifications sur votre ordinateur en respectant les règles sur le code
- Executé les tests afin d'etre sur de ne rien avoir cassé.
- Faite un ```git add``` de vos modification en veillant à n'avoir rien raté avec un ```git status```
- Committez en respectant les règle du .gitmessage, tous commit ne les respectants pas est refusé.

Ne jamais mettre des mots de passe, token, information privé, ... dans un commit.
Ne mettez pas plusieurs modifications dans un commit, faite des commit séparé.
Tous commit doit avoir être fait avec un nom d'utilisateur, un usermail et une email.
Si possible signé les commit avec pgp.


