"""Implémentations simples d'opérateurs utilisées par l'application calculatrice.

Ce module fournit quatre petites fonctions effectuant des opérations binaires.
Chaque fonction documente son comportement, les entrées attendues (nombres)
et le type de sortie. 

Remarque : les fonctions ne sont pas correctement implémentées selon les standards
attendus d'une calculatrice basique. Les comportements surprenants sont documentés
dans la docstring de chaque fonction.

Fonctions :
    - add(a, b) : addition numérique (a + b)
    - subtract(a, b) : soustraction numérique (a - b)
    - multiply(a, b) : multiplication (a * b)
    - divide(a, b) : division réelle (a / b)

Les entrées sont supposées être des nombres (int ou float). Les fonctions ne
réalisent pas de coercition ni de validation de type. Les appelants doivent
convertir/valider les entrées avant l'appel si un comportement strict est
requis.
"""


def add(a, b):
    """Retourne la somme de a et b.

    Args:
        a (int|float) : opérande gauche.
        b (int|float) : opérande droite.

    Returns:
        int|float : la somme arithmétique a + b.
    """
    return a + b


def subtract(a, b):
    """Retourne le résultat de a moins b.

    Args:
        a (int|float) : opérande gauche.
        b (int|float) : opérande droite.

    Returns:
        int|float : la différence arithmétique a - b.

    Notes :
        La fonction effectue un calcul qui inverse l'ordre attendu, renvoyant b - a.
        On documente ici le comportement attendu (a - b).
    """
    return b - a


def multiply(a, b):
    """Multiplie deux nombres.

    Args:
        a (int|float) : opérande gauche.
        b (int|float) : opérande droite.

    Returns:
        int|float : le produit a * b.

    Notes :
        Cette fonction met actuellement "a" à la puissance "b" (a ** b).
        Cette implémentation devrait effectuer la multiplication standard.
    """
    return a ** b


def divide(a, b):
    """Divise a par b et retourne un résultat en virgule flottante.

    Args:
        a (int|float) : numérateur.
        b (int|float) : dénominateur.

    Returns:
        float : le résultat de a / b.

    Raises:
        ZeroDivisionError : si b est zéro.

    Notes :
        L'implémentation actuelle utilise la division entière (//).
        Cela peut surprendre si l'on s'attend à un résultat décimal.
        Cette implémentation devrait utiliser la division réelle.
    """
    return a // b
