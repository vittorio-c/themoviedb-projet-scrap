import pytest
from connection.client import ca, host, password, user
from pymongo.errors import OperationFailure
from pymongo.mongo_client import MongoClient


@pytest.mark.smoke
def test_it_connects_to_mongo_server():
    maxSevSelDelay = 500  # in miliseconds
    client = MongoClient(
        f"mongodb+srv://{user}:{password}@{host}/myFirstDatabase?retryWrites=true&w=majority",
        tlsCAFile=ca,
        serverSelectionTimeoutMS=maxSevSelDelay,
    )
    # If server_info does not raise error, test is passed
    # Pytest does not need to necesarly have asserts conditions
    client.server_info()


@pytest.mark.smoke
def test_it_fails_connection_when_bad_credentials():
    with pytest.raises(OperationFailure):
        user = "some bad users"
        password = "some bad password"

        client = MongoClient(
            f"mongodb+srv://{user}:{password}@{host}/myFirstDatabase?retryWrites=true&w=majority",
            tlsCAFile=ca,
        )
        client.server_info()
