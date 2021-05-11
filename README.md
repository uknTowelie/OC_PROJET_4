# OC_PROJET_4

Ce programme est une application hors-ligne permettant de gérer des tournois d'échecs.</br>
Les tournois se déroule avec selon le système suisse et les joueurs sont initialement placé selon leur classement (elo).</br>
Les différents données des tournois précédents ainsi qu'une liste des participants sont stockés dans une base de donnée local.

# Language utilisé

Ce programme utilise la version 3.8.5 de [Python]("https://www.python.org/")

# Environement virtuel

Installer un environement virtuel :

## Sous Linux/Mac
<hr/>
Installation :

    python3 -m venv .venv

Activation :

    source .venv/bin/activate

## Sous Windows
<hr/>

Installation : 

    py -3 -m venv .venv

Activation :

    .venv/scripts/activate

# Package et modules

Pour installer les différents packages via [pip]("https://fr.wikipedia.org/wiki/Pip_(gestionnaire_de_paquets)") :

    pip install -r requirements.txt

# Exécuter le programme

Commande a éxécuter dans le dossier racine du projet :

    python3 __main__.py

# Aide 

Depuis le mùenu principale vous pourrez créer un nouveaux tournoi ou depuis la base de donnée afficher ou charger un tournoi

Cela n'est plus possible lorsqu'un tournoi est démarré

Pour finir un round chaque match doit être terminé

Pour finir un tournoi chaque round doit être terminé

Des qu'un tournoi est créé il peux etre enregister et est automatiquement enregister lorsqu'il est terminé

La base de donnée est automatiquement enregisté lorsque l'on quitte le programme depuis un menu

