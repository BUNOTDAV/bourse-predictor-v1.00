# Bourse Predictor v1.00

Ce projet analyse les actualités des actions du CAC40 et S&P500 pour prédire les hausses probables.

## Installation

1. Crée un environnement virtuel :
    python -m venv venv

2. Active-le :
    - Windows : venv\Scripts\activate
    - Mac/Linux : source venv/bin/activate

3. Installe les dépendances :
    pip install -r requirements.txt

## Utilisation

1. Remplace `YOUR_NEWSAPI_KEY` dans main.py par ta clé depuis https://newsapi.org.
2. Lance le script :
    python main.py

## Résultat

Le script affichera les actions triées par probabilité et donnera une alerte si une action a ≥ 90% de probabilité de hausse.
