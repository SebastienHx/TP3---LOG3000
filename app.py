"""Point d'entrée de l'application web pour une petite calculatrice.

Ce module définit une application Flask servant une interface de
calculatrice simple (`templates/index.html`). Il expose une route unique
('/') acceptant GET et POST. Le gestionnaire POST lit une expression
depuis le formulaire, analyse une unique opération binaire, convertit
les opérandes en nombres et délègue aux implémentations arithmétiques
dans `operators`.

Hypothèses et comportement :
    - Les expressions attendues ont la forme : <nombre><op><nombre>, ex. "3 + 4".
    - Une seule opérateur est autorisé par expression ; les espaces sont ignorés.
    - Les opérandes sont parsées avec float() ; les appelants doivent fournir
        le format attendu pour les entiers ou décimaux.
    - Les messages d'erreur sont affichés dans l'interface via la variable `result`.

Dépendances :
    - Flask (importé comme from flask import Flask, request, render_template)
    - Le module `operators` situé dans le même répertoire et fournissant
        les fonctions arithmétiques : add, subtract, multiply, divide.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Mapping de symbole d'opérateur vers l'implémentation.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """Analyse et évalue une expression binaire simple fournie sous forme de chaîne.

    La fonction accepte des chaînes comme "3+4", " 5 * 7 " et retourne
    le résultat numérique de l'opération trouvée appliquée aux deux opérandes.

    Args :
        expr (str) : expression d'entrée ; doit contenir exactement un opérateur
            présent dans la table `OPS` et deux opérandes numériques.

    Returns :
        int|float : résultat retourné par la fonction opérateur correspondante.

    Raises :
        ValueError : si l'entrée est vide, mal formée, contient zéro ou plus
            d'un opérateur, ou si les opérandes ne peuvent être convertis en nombres.

    Remarques d'implémentation :
        - Les espaces sont supprimés avant l'analyse.
        - La fonction effectue un balayage linéaire pour trouver l'opérateur
          et ne supporte pas les parenthèses, signes unaires ni les expressions
          arithmétiques complexes.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Supprime les espaces pour simplifier la recherche de l'opérateur.
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche de l'opérateur unique dans l'expression. Si plusieurs opérateurs
    # sont trouvés, on renvoie une erreur.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # L'opérateur doit exister et ne peut pas être le premier ou le dernier caractère.
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
    # Utilise float() pour accepter à la fois des entiers et des décimaux.
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Délègue à l'implémentation de l'opérateur ; Cela peut lever
    # ZeroDivisionError pour une division par zéro ou d'autres erreurs spécifiques.
    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Route Flask pour l'interface de la calculatrice.

    GET : rend la page de la calculatrice avec un résultat vide.
    POST : lit le champ de formulaire nommé 'display', l'évalue via
    `calculate`, et transmet le résultat (ou un message d'erreur) au
    template sous la variable `result`.

    Returns :
        str : page HTML rendue à partir de `templates/index.html`.
    """
    result = ""
    if request.method == 'POST':
        # Le champ du formulaire s'appelle 'display' dans le template HTML.
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # Affiche un message d'erreur lisible à l'utilisateur.
            result = f"Error: {e}"
    return render_template('index.html', result=result)


if __name__ == '__main__':
    # Lance le serveur de développement local.
    app.run(debug=True)