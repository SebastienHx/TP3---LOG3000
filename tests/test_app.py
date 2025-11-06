"""Tests unitaires pour la fonction `calculate` du module `app`.

Ces tests valident le parsing et l'évaluation d'expressions arithmétiques
simples de la forme "<nombre><op><nombre>" (ex. "3+4"). Ils couvrent les
cas d'addition, de soustraction, de multiplication et de division ainsi que
les erreurs attendues (entrée vide, opérandes non numériques, plusieurs
opérateurs, division par zéro).

Remarque sur l'import des modules : lors de l'exécution via pytest depuis
un répertoire quelconque, s'assurer que la racine du projet est dans
`sys.path` permet d'importer `app` en tant que module de niveau racine.
"""

import os
import sys
import pytest

# Ajoute la racine du projet au début de sys.path afin que les imports
# comme `from app import calculate` fonctionnent indépendamment du CWD.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import calculate


@pytest.mark.parametrize("expr,expected", [
    ("3+4", 7.0),
    (" 5 - 2 ", 3.0),
    ("2*3", 6.0),
    ("7/2", 3.5),
])
def test_calculate_ok(expr, expected):
    """Vérifie que `calculate` évalue correctement des expressions simples.

    Couvre plusieurs opérateurs via paramétrisation : +, -, * et /.
    On compare la valeur retournée (float/int) avec la valeur attendue.
    """
    assert calculate(expr) == expected


def test_calculate_empty():
    """Entrée vide — on s'attend à une ValueError.

    Le code doit rejeter les chaînes vides ou non-strings.
    """
    with pytest.raises(ValueError):
        calculate("")


def test_calculate_multiple_ops():
    """Expression contenant plusieurs opérateurs — erreur attendue.

    La spécification impose une seule opération binaire par expression.
    """
    with pytest.raises(ValueError):
        calculate("1+2-3")


def test_calculate_non_numeric():
    """Opérandes non numériques — doit lever ValueError lors du parsing.

    Le code utilise float() pour convertir les opérandes ; si cela échoue,
    la fonction doit remonter une ValueError.
    """
    with pytest.raises(ValueError):
        calculate("a+b")


def test_calculate_divide_by_zero():
    """Division par zéro — on attend une ZeroDivisionError provenant de
    l'implémentation de l'opérateur division dans `operators.py`.
    """
    with pytest.raises(ZeroDivisionError):
        calculate("1/0")
