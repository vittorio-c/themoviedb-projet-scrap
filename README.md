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
TEST

 - Scrapping

Des tests ont été créés pour le script scrapper.py qui s'occupe d'aller scrapper le site "https://www.themoviedb.org/" afin de populer la base de données. Ils s'occupent de vérifier si le squelette du site cible a changé afin de revoir le scrapping au besoin. Ces tests se trouvent dans le fichier /tests/scrapper/test_scrapper.py

On peut constater le rapport suivant :

![rapport1 jpg](https://user-images.githubusercontent.com/75723296/146558506-16a70970-439b-490b-802f-5636908a7b3a.png)

 - Locust (Tests de montée en charge)

Des tests via l'outil Locust ont été effectués afin connaître la solidité du code et de son architecture. Ils ont été exécutés avec 10000 / 50000 / 100000 utilisateurs. On peut voir le rapport suivant représentant 100000 utilisateurs se connectant à l'application web tournant en local :

![locust1](https://user-images.githubusercontent.com/75723296/146559527-04a55be8-818d-4add-9859-3def21af75cd.png)
  ![locust2](https://user-images.githubusercontent.com/75723296/146559555-ef9ead60-0f73-432c-b671-295ed309f0c5.png)
  ![locust3](https://user-images.githubusercontent.com/75723296/146559578-aa2f22a2-314f-4b5b-ac7c-574c35372eda.png)
  



