"""Fichier d'exemple"""


def add(a, b):
    """Description rapide de la fonction

    Description plus long. Quand faut il utilisé votre fonction ...

    :Example:
    >>> add(1, 1)
    2

    :param a: Paramètre 1
    :type a: float/int
    :param b: Paramètre 2
    :type b: float/int
    :return: Valeur de retour
    :rtype: float/int

    :raise TypeError: Si a ou b n'est pas un float/int
    """
    # Verification des arguments
    if not (isinstance(a, float) or isinstance(a, int) and isinstance(b, float) or isinstance(b, int)):
        raise TypeError

    # Calcul
    c = a + b

    return c
