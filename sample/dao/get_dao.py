from sample.postgres_connection import postgres_connect
from sample.dao.postgres_dao import PostgresDAO


def get_db(self, db):
    if db == "postgres":
        db = postgres_connect()
        return PostgresDAO(db)
    elif db == "mongo":
        pass
