import datetime
import os
import sys

import certifi
import pymongo
from dotenv import dotenv_values

ca = certifi.where()

config = dict(dotenv_values(".env"))

try:
    # Local value... (from .env file)
    password = config["MONGODB_ATLAS_PASSWORD"]
except KeyError:
    # Env value...
    password = os.environ["MONGODB_ATLAS_PASSWORD"]

try:
    user = config["MONGODB_ATLAS_USER"]
except KeyError:
    user = os.environ["MONGODB_ATLAS_USER"]

try:
    host = config["MONGODB_ATLAS_HOST"]
except KeyError:
    host = os.environ["MONGODB_ATLAS_HOST"]

client = pymongo.MongoClient(
    f"mongodb+srv://{user}:{password}@{host}/myFirstDatabase?retryWrites=true&w=majority",
    tlsCAFile=ca,
)
