from abc import ABC
import psycopg2
from psycopg2 import Error
from sample.dao.dao_abc import DAO


class postgresDAO(DAO):

    def __init__(self, db):
        self.db = db


if __name__ == "__main__":
    pass
