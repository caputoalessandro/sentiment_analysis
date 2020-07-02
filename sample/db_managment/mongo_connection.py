from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from sample.db_managment.config import config


def mongo_connect() -> MongoClient:
    """ Connect to the MongoDB database server """
    conn = None
    try:
        conn = MongoClient('localhost', 27017)

    except ConnectionFailure:
        print("Server not available")

    finally:
        return conn
