from sample.dao.dao_abc import DAO
from sample.resources.resources import Resources


class PostgresDAO(DAO):

    def __init__(self, db):
        self.db = db

    def upload_word(self, resource_data: Resources):
        pass

