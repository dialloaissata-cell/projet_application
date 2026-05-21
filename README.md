# Projet Application

## Présentation

Ce projet est une application simple avec un backend en Python utilisant FastAPI. Le backend fournit une API qui sert des données d'étudiants au format JSON, générées à partir du fichier `donnees_propres.csv`.

## Structure du projet

- `backend/`
  - `main.py` : serveur FastAPI qui expose des routes web.
  - `data_json.py` : script qui convertit le fichier CSV `donnees_propres.csv` en JSON (`etudiants.json`).
  - `etudiants.json` : données des étudiants au format JSON.
- `donnees_propres.csv` : fichier source contenant les données des étudiants nettoyées.
- `frontend/` : dossier prévu pour l’interface utilisateur (actuellement vide).

## Installation

1. Ouvrir un terminal dans le dossier du projet.
2. Activer l'environnement virtuel si nécessaire :
   - `source backend/venv~/bin/activate`
3. Installer FastAPI et Uvicorn si ce n’est pas déjà fait :
   - `pip install "fastapi[standard]" uvicorn`

## Génération des données JSON

Avant de lancer l'API, exécuter le script de conversion :

```bash
cd backend
python data_json.py
```

Cela crée ou met à jour le fichier `etudiants.json` à partir de `donnees_propres.csv`.

## Lancement du backend

Exécuter le serveur FastAPI avec Uvicorn :

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Puis ouvrir dans le navigateur :

- `http://127.0.0.1:8000/` pour vérifier que l'API fonctionne
- `http://127.0.0.1:8000/docs` pour accéder à la documentation Swagger

## Routes disponibles

- `GET /` : page d'accueil de l'API, renvoie un message de confirmation.
- `GET /etudiants` : renvoie la liste des étudiants depuis `etudiants.json`.

## Utilisation

Le backend peut être utilisé par un frontend ou tout client HTTP pour récupérer les données des étudiants au format JSON. Le dossier `frontend/` est prévu pour ajouter l'interface utilisateur ultérieurement.

## Remarques

- Si le dossier `frontend/` reste vide, le projet fonctionne uniquement comme API backend.
- Les données sont stockées dans `etudiants.json` après conversion.
- FastAPI permet de développer facilement l'API et de visualiser la documentation automatiquement.
