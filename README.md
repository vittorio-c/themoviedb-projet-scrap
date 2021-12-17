# themoviedb-projet-scrap

## Steps to get started

- If you want to work in isolated environment (optional) :

`python3 -m venv env`

- Install dependencies :

`pip install -r requirements.txt`

- Fill env values in .env (see .env.example)

- (optional) Lauch the scrapper :

`python scrapper/scrapper.py`

- Lauche the backend server locally :

`FLASK_APP=app FLASK_ENV=development flask run`

- Install front dependencies : 

`yarn install`

- Launch front server : 

`yarn serve`

- Access the app from : `http://localhost:8080/`

# Tests

## Etapes de réalisation du TP tests/automatisation

### Mock de la BDD

- Installation d'un package dédié au mock de BDD Mongo dans python : `mongomock`. Raison : il aurait été trop couteux et long de devoir réimplémenter à l'aide de `monkeypatch` toutes les méthodes du package `pymongo` pour interroger une BDD mockée (ex: la méthode `aggregate()` d'une `Collection` utilisée dans `queries/movies.py`. `mongomock` s'occupe de tout ce _boilerplate_ pour nous, et nous pouvons nous concentrer sur l'essentiel.
- Inclusion de la fixture `setup_mocked_db` en `autouse=True`, afin que tous les tests bénéficient d'une DB mockée

### Test d'un scrapper pour détecter les changements de balises dans le site cible

- Instanciation d'un driver dédié compatible avec la CI sur github
- Tests de plusieurs pages importantes pour s'assurer que le site n'a pas changé de façon importante
- Plusieurs tests _parametrized_ afin de tester la présence de balises CSS spécifiques, utilisées dans le scrapper principal
- A noter que : Les tests du fichier `tests/scrapper/test_scrapper.py` ne peuvent être pris en compte par le test coverage, car ils n'appellent pas directement les fonctions du `scrapper.py`. 
- Un rapport de tests au format HTML a été créé :

![rapport1 jpg](https://user-images.githubusercontent.com/75723296/146566026-bbc4394c-38f0-4acb-ac33-e10ab8c73f80.png)

### Mise en place d'une CI sur Github avec les Github Actions

- Création d'un fichier de configuration `.github/workflows/tests.yml`
- Déclaration des pipelines de la CI : "Set up Python" => "Install dependencies" => "Analysing the code with black & isort" => "Test with Pytest"
- Définition d'un ordre pour le lancement des tests, afin de lancer les smoke tests en premier, et d'arrêter la CI si ceux-ci échouent : `pytest -v -m smoke && pytest -v -m "not smoke"` (taggage des smoke test avec `@pytest.mark.smoke`)
- La pipeline se déclenche à chaque push sur une branche.
- L'échec des tests avec pytest durant la pipeline bloque de facto la fusion de la branche dans `main`
- Importation des secrets dans Github (identifiants de connexion à la BDD) afin que la CI ait accès à la BDD de production et ne pas bloquer certains tests.

### Ecriture de tests unitaires avec utilisation des fixtures et de la _parametrization_

- Déclaration de fixtures partagées par tous les modules dans `tests/conftest.py`
- Utilisation de plusieurs tests _paramatrized_ afin de pouvoir tester plusieurs ensembles de données
- Typologie des tests écrits :
  - Smoke tests
  - Tests des routes
  - Tests de la pagination 
  - Tests des fonctions CRUD liées à la BDD
- Reste à faire : les tests d'intégration + les tests _end to end_

### Locust

- Installation de locust pour les tests de montée en charge
- Tests avec 3 scénarios d'utilisation : 10 000, 50 000 et 100 000 utilisateurs faisant des requêtes à la fois sur site.
- Rapports de tests générés en HTML et accessibles sur la route `/report`

### VueJS

- Migration du projet sur VueJS + Tailwind, en préservant l'existant (templates jinja servis depuis Flask)
- Projet VueJS disponible sur `http://localhost:8080` , en mode SPA
- Le backend devient une API seule
- Reste à faire : migration de toutes les routes de backend sur l'api `/api/my_route>`

## Coverage

**45 %** : ce chiffre ne tient pas compte des tests effectués sur le scrapper, qui ne peuvent pas être inclus par le coverage de pytest (pas d'appels directs aux fonctions du scrapper). Par conséquent, nous sommes plus dans les 60%.

[Coverage](./reports_tests/cover_2.png)

[Détails](./reports_tests/cover_1.png)

[Détails 2](./reports_tests/cover_3.png)

# Misc

Model de donnée pour les films : 

```json
{
  "_id": "https://www.themoviedb.org/movie/527774-raya-and-the-last-dragon",
  "title": "xxxx",
  "url": "https://www.themoviedb.org/movie/527774-raya-and-the-last-dragon",
  "release_year": 2001,
  "user_rating": 80,
  "picture_url": "<photo-url>",
  "genres": ["animation", "thriller"],
  "tags": ["warrior", "kung-fu"],
  "budget": 24000000,
  "revenues": 150000000,
  "profit": "<budget - revenues>",
  "duration": "1h 54m",
  "country_releases": ["DE", "FR", "ES", "GB"],
  "director": "Georges Martin",
  "artists": [
    {
      "_id": "https://www.themoviedb.org/person/1663195-kelly-marie-tran",
      "role": "Raya (voice)",
      "name": "Carole Sergeant"
    },
    {
      "_id": "https://www.themoviedb.org/person/1663195-kelly-marie-tran",
      "role": "Raya (voice)",
      "name": "Carole Sergeant"
    },
    {
      "_id": "https://www.themoviedb.org/person/1663195-kelly-marie-tran",
      "role": "Raya (voice)",
      "name": "Carole Sergeant"
    }
    ]
}
```
