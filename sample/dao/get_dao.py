from sample.db_managment.postgres_connection import postgres_connect
from sample.dao.postgres_dao import PostgresDAO


def get_db(db : str):
    if db == "postgres":
        db = postgres_connect()
        return PostgresDAO(db)
    elif db == "mongo":
        pass
