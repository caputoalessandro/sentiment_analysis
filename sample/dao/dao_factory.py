import psycopg2
from sample.dao.postgres_dao import postgresDAO
from sample.dao.postgres_connection import postgres_connect


def get(self, db):
    if db == "postgres":
        db = postgres_connect()
        return postgresDAO(db)

