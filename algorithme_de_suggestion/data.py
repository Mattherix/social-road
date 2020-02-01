"""
Fichier avec des données de test pour l'agorithme de suggestion

Organisation des données:

liste_info_post = [<post>, <post>, ...]

<post>: Tuple[<post_id>, <user_list>] Un post effectué

<post_id>: int Un identifiant numerique pour le post
<user_list>: List[Tuple[<vue>, <user>], Tuple[<vue>, <user>], ...] La liste des utilisateur ayant vue le post

<vue>: int Le nombre de foit ou l'utilisateur a vue le post
<user>: Dict[
    'user_id': <user_id>,
    'note': <note>,
    'like': <like>,
    'like_list': <like_list>,
    'friend': <friend>,
]

<user_id>: int Un identifiant numerique pour l'utilisateur
<note>: int La note de l'utilisateur
<like>: bool A True si l'utilisateur a like sinon False
<like_list>: List[<post_id>, <post_id>, ...] La liste des posts que l'utilisateur à like
<friend>: List[<user_id>, <user_id>, ...] La liste des amis de l'utilisateur

"""
