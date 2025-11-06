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

   Des tests unitaires vont être ajoutés pour couvrir la logique de
   parsing et les opérations (par exemple : `calculate`, `operators`).
   Voici comment exécuter les tests une fois qu'ils seront présents :

   1. Installer les dépendances de test :

   ```cmd
   pip install pytest
   ```

   2. Lancer les tests depuis la racine du projet :

   ```cmd
   pytest -q
   ```

   ## Flux de contribution

   Ce projet suit un flux simple de contribution. Règles recommandées :

   - Branches :
     - `main` : branche de production stable.
     - Créez une branche de travail nommée `feature/<nom>` ou `fix/<nom>` pour
       chaque nouvelle fonctionnalité ou correction.

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

   ````