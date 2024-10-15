
# Série d'Exercices Flask

Ce dépôt contient une série d'exercices pratiques pour apprendre et maîtriser Flask, un micro-framework web Python.

## Objectifs

Les exercices sont conçus pour :
- Comprendre les concepts de base de Flask.
- Développer des applications web simples avec des routes et des templates.
- Intégrer des formulaires et gérer les requêtes HTTP (GET et POST).
- Gérer la base de données avec SQLAlchemy.
- Maîtriser l'authentification utilisateur (sessions, cookies).

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les outils suivants :
- [Python 3.8+](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/) (`pip install flask`)
- [SQLAlchemy](https://www.sqlalchemy.org/) (`pip install SQLAlchemy`)

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/sabriallani/Serie_exercices_Flask.git
   cd Serie_exercices_Flask
   ```

2. Créez un environnement virtuel (optionnel mais recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

3. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

## Structure du projet

- `app.py` : Le fichier principal qui contient l'initialisation de l'application Flask et les routes.
- `templates/` : Dossier contenant les fichiers HTML pour les templates.
- `static/` : Dossier contenant les fichiers statiques comme les fichiers CSS et JavaScript.
- `exercices/` : Dossier où sont organisés les différents exercices.

## Liste des Exercices

1. **Exercice 1** : Introduction à Flask et création d'une première route.
2. **Exercice 2** : Utilisation des templates avec Jinja2.
3. **Exercice 3** : Gestion des formulaires et des requêtes POST.
4. **Exercice 4** : Gestion des sessions et des cookies.
5. **Exercice 5** : Connexion à une base de données avec SQLAlchemy.
6. **Exercice 6** : Authentification utilisateur.

Chaque exercice est accompagné de son énoncé et des instructions spécifiques pour la mise en œuvre.

## Exécution des exercices

1. Lancez le serveur Flask :
   ```bash
   flask run
   ```

2. Ouvrez votre navigateur et accédez à [http://127.0.0.1:5000](http://127.0.0.1:5000) pour voir l'application en action.

## Contribuer

Les contributions sont les bienvenues ! Si vous avez des suggestions ou trouvez des problèmes, n'hésitez pas à ouvrir une issue ou à proposer une pull request.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
