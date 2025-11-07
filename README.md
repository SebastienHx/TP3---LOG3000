# Calculatrice Web (Flask)

## Objectif

Créer une **calculatrice web simple** avec **Flask (Python)**, hébergée sur **GitHub**, en appliquant de bonnes pratiques de gestion de version, documentation et collaboration.
L’application permet de faire des opérations de base : addition, soustraction, multiplication et division.

## Équipe #05

- Membres: Sébastien Brossier, Jason Chen, Samy Cherifi

---

## Prérequis d’installation

Avant de lancer le projet, assurez-vous d’avoir installé :

* [Python 3.10+](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [Git](https://git-scm.com/)

## Instructions d’installation

1. **Cloner le dépôt GitHub**

   ```bash
   git clone https://github.com/SebastienHx/TP3---LOG3000.git
   ```

2. **Créer et activer un environnement virtuel** (Recommendé)

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l’application**

   ```bash
   python app.py
   ```

   Puis ouvrez votre navigateur à l’adresse :

   ```
   http://127.0.0.1:5000
   ```
---

## Tests

Des tests unitaires sont fournis dans le répertoire `tests/` pour couvrir
la logique principale : parsing d'expressions et opérations arithmétiques.

Fichiers clés :

- `tests/test_app.py` : tests pour la fonction `calculate` (dans `app.py`).
  - Cas couverts : opérations valides (addition, soustraction,
    multiplication, division), entrée vide, plusieurs opérateurs,
    opérandes non numériques, division par zéro.
- `tests/test_operators.py` : (si présent) tests pour les fonctions
  arithmétiques (`add`, `subtract`, `multiply`, `divide`) du module
  `operators.py`.

Instructions pour exécuter les tests :

1. Exécuter les instructions d'installations :

- S'assurer que lance correctement


2. Exécutez la suite de tests depuis la racine du projet :

```bat
python -m pytest -q
```

Remarque : `tests/test_app.py` ajoute la racine du projet à `sys.path`
au démarrage des tests afin de pouvoir importer `app` en tant que
module de niveau racine. Si vous rencontrez des problèmes d'import,
vérifiez votre CWD et l'environnement virtuel activé.

## Flux de contribution

Ce projet suit un flux simple de contribution. Règles recommandées :

- Branches :
  - `main` : branche de production stable.
  - Créez une branche de travail nommée `feature/<nom>` pour
    chaque nouvelle fonctionnalité.
  - Créez une branche de travail nommée `<numéro de l'issue> - <Titre de l'issue>`
    pour la correction d'une issue.   

- Pull Requests (PR) :
  - Ouvrez une PR depuis votre branche de travail vers `main`.
  - Ajoutez une description claire du changement, les tests ajoutés
    et les étapes de vérification.
  - Affectez au moins une relecture par un autre membre de l'équipe
    avant de fusionner.

- Issues :
  - Ouvrez une issue pour signaler un bug ou proposer une fonctionnalité.
  - Liez les PR aux issues correspondantes (ex. "Fixes #12").

- Revue et validation :
  - Les PR doivent passer les tests.
  - Utilisez des commits atomiques et des messages clairs.

Ces règles peuvent évoluer selon les besoins du projet ; documentez
tout changement majeur dans ce `README.md`.
