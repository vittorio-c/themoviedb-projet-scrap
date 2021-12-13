import sys
import datetime
import pymongo
from dotenv import dotenv_values

config = dict(dotenv_values(".env"))

# password = config["MONGODB_ATLAS_PASSWORD"]
# user = config["MONGODB_ATLAS_USER"]
# host = config["MONGODB_ATLAS_HOST"]

# client = pymongo.MongoClient("mongodb+srv://{}:{}@{}/myFirstDatabase?retryWrites=true&w=majority".format(user, password, host))
