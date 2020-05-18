import psycopg2
from sample.dao.postgres_dao import postgresDAO
from sample.dao.postgres_connection import postgres_connection


class get_dao():

    def get(self, db):
        if db == "postgres":
            connection = postgres_connection()
            db = connection
            return db

