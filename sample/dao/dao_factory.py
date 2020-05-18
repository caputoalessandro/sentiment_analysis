from sample.dao.postgres_dao import postgresDAO


class get_dao():

    def get(self,db):
        if db == "postgres":
            return postgres_dao
        elif db == "mongo":
            return mongo_dao
