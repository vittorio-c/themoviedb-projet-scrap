import datetime
import sys

import certifi
import pymongo
from dotenv import dotenv_values

ca = certifi.where()

config = dict(dotenv_values(".env"))

password = config["MONGODB_ATLAS_PASSWORD"]
user = config["MONGODB_ATLAS_USER"]
host = config["MONGODB_ATLAS_HOST"]

client = pymongo.MongoClient(
    f"mongodb+srv://{user}:{password}@{host}/myFirstDatabase?retryWrites=true&w=majority",
    tlsCAFile=ca,
)
