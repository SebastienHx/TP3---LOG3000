# templates/

## But du répertoire

Contient les templates utilisés pour rendre les pages web de l'application Flask. 
Fournit l'interface pour la calculatrice. Les boutons concatènes les chiffres et les 
opérateurs afin de l'envoyer au serveur qui s'occupe du calcul.

## Fichiers principaux
- `index.html` : template principal affichant la calculatrice et le
  résultat des opérations.

## Dépendances

Ce template dépend des éléments suivants pour fonctionner correctement :

- `static/style.css` : feuille de style référencée via `url_for('static', filename='style.css')`.
- Variable de contexte Jinja2 : `result` — fournie par la route Flask pour afficher
  soit la valeur calculée, soit un message d'erreur.
- Route Flask attendue : `/` (définie dans `app.py`) qui traite GET et POST.
- Champ de formulaire attendu : le template envoie un champ nommé `display`
  contenant l'expression à évaluer (côté serveur, `request.form.get('display')`).
- Aucun script externe ou bibliothèque JS n'est requis ; le JavaScript utilisé
  est en ligne dans `index.html` (fonctions `appendToDisplay` et `clearDisplay`).

## Pour les développeurs
- Si vous modifiez les noms de variables envoyées au template (par
  ex. `result`), mettez à jour le template en conséquence.