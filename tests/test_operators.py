"""Tests unitaires pour les fonctions arithmétiques du module `operators`.

Ce module vérifie les opérations de base implémentées dans
`operators.py`: `add`, `subtract`, `multiply`, et `divide`.
Les tests couvrent des cas sur des entiers et des flottants ainsi que
le comportement attendu en cas de division par zéro.
"""

import os
import sys
import pytest

# Permet d'importer le module `operators` depuis la racine du projet
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from operators import add, subtract, multiply, divide


def test_add():
    """Addition — vérifie la somme d'entiers et de flottants.

    On attend :
    - add(3, 4) == 7
    - add(2.5, 1.5) == 4.0
    """
    assert add(3, 4) == 7
    assert add(2.5, 1.5) == 4.0


def test_subtract():
    """Soustraction — vérifie la différence pour int et float.

    Exemples : subtract(10, 3) == 7 et subtract(5.0, 2.5) == 2.5
    """
    assert subtract(10, 3) == 7
    assert subtract(5.0, 2.5) == 2.5


def test_multiply():
    """Multiplication — vérifie le produit pour int et float.

    Exemples : multiply(2, 3) == 6 et multiply(1.5, 2) == 3.0
    """
    assert multiply(2, 3) == 6
    assert multiply(1.5, 2) == 3.0


def test_divide():
    """Division — vérifie la division normale (float résultat si nécessaire).

    Exemples : divide(7, 2) == 3.5 et divide(6.0, 3.0) == 2.0
    """
    assert divide(7, 2) == 3.5
    assert divide(6.0, 3.0) == 2.0


def test_divide_by_zero():
    """Division par zéro — l'implémentation doit lever ZeroDivisionError.

    Ce test vérifie que la fonction `divide` ne masque pas l'exception
    de division par zéro et la remonte correctement.
    """
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
