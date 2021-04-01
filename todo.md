# Objectis : 

**Mission 1**

- Scrapper TheMovieDb.org pour récupérer des informations sur 1000 films

**Mission 2**

- Nettoyer et structurer les données collectées
- Créer une DB MongoDB et y injecter les données : utiliser Atlas pour avoir une BDD commune

**Mission 3**

- Réaliser plusieurs Qry qui répondent à des questions-métiers relevées à partir de vos données.  
- Il va falloir faire des requêtes complexes d'agrégation 

**Mission 4**
- Présenter les résultats des requêtes sur une interface web en local

# Liste des infos à récupérer sur les films

- Nom du film
- Date de sortie
- Note des utilisateurs (score)
- Photos
- Tags
- Recette
- Budget
- Catégories
- Acteurs : nom + prénom + lien vers la fiche
- Réalisateur
- Durée
- Commentaires (si présents)
- Critiques (si présents)
- Diffusion internationale : nb de pays diffusés

# Liste des tâches :

*Vittorio* :

- Créer une DB MongoDB et y injecter les données : 
    - schéma : quelles collections  + quel type de document ? 
    - utiliser Atlas pour avoir une BDD commune
    - S'assurer qu'on n'insère pas deux fois la même donnée (utiliser l'url comme clé unique)

*Bastien / Anastasia / Wissem en support*

- Scrapper TheMovieDb.org pour récupérer des informations sur 1000 films
- Récupérer les infos suivantes : 
    - Nom du film
    - Date de sortie
    - Note des utilisateurs (score)
    - Photos
    - Tags
    - Recette
    - Budget
    - Catégories
    - Acteurs : nom + prénom + lien vers la fiche
    - Réalisateur
    - Durée
    - Commentaires (si présents)
    - Critiques (si présents)
    - Diffusion internationale : nb de pays diffusés

*Wissem (une fois que le scrapping est fait)*

- Réaliser plusieurs Qry qui répondent à des questions-métiers relevées à partir de vos données.  
- Il va falloir faire des requêtes complexes d'agrégation 

*Vittorio*

- Structurer le projet en mode web

*Ensemble*

- Présenter les résultats des requêtes sur une interface web en local (matpotlib, seaborn, etc.)
