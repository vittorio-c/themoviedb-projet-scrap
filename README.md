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

TEST

Des tests ont été créés pour le script scrapper.py qui s'occupe d'aller scrapper le site "https://www.themoviedb.org/" afin de populer la base de données. Ils s'occupent de vérifier si le squelette du site cible a changé afin de revoir le scrapping au besoin. Ces tests se trouvent dans le fichier /tests/scrapper/test_scrapper.py

On peut constater le rapport suivant :

![alt text](https://github.com/vittorio-c/themoviedb-projet-scrap/blob/main/rapport1.png?raw=true)

