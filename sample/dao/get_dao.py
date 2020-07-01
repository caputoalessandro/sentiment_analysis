from sample.db_managment.postgres_connection import postgres_connect
from sample.dao.postgres_dao import PostgresDAO
from sample.dao.mongo_dao import MongoDAO
from sample.db_managment.mongo_connection import mongo_connect


def get_db(db: str):
    if db == "postgres":
        db = postgres_connect()
        return PostgresDAO(db)
    elif db == "mongo":
        db = mongo_connect()
        return MongoDAO(db)
