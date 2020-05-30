from sample.dao.dao_abc import DAO
from sample.resources.lexical_resources import LexicalResources
import psycopg2


class PostgresDAO(DAO):

    def __init__(self, db):
        self.db = db

    def upload_words(self, resources: LexicalResources):
        try:
            cursor = self.db.cursor()

            records = resources.get_records()

            sql_insert_query = """ INSERT INTO words (word, sentiment, resource, occurences) 
                                   VALUES (%(word)s, %(sentiment)s, %(resource)s, 1) 
                                   ON CONFLICT (word, sentiment, resource) DO UPDATE 
                                   SET occurences = words.occurences + 1 
                                   WHERE 1 = 1
                                   AND words.word = %(word)s
                                   AND words.sentiment = %(sentiment)s
                                   AND words.resource = %(resource)s
                                   """


            # executemany() to insert multiple rows rows
            result = cursor.executemany(sql_insert_query, records)
            self.db.commit()
            print(cursor.rowcount, "Record inserted successfully into mobile table")

        except (Exception, psycopg2.Error) as error:
            print("Failed inserting record into mobile table {}".format(error))

        finally:
            # closing database self.db.
            if self.db:
                cursor.close()
                self.db.close()
                print("PostgreSQL self.db is closed")

