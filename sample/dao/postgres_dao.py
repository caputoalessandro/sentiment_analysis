from sample.dao.dao_abc import DAO
from sample.resources.resources import Resources
from sample.processing.twitter_processor import TweetData
from typing import List
from dataclasses import astuple
import psycopg2


class PostgresDAO(DAO):

    def __init__(self, db):
        self.db = db

    def upload_words(self, resources: Resources):
        try:
            cursor = self.db.cursor()

            records = resources.get_word_records()

            sql_insert_query = """ INSERT INTO words (word, sentiment, resource, occurences, tweet_freq) 
                                   VALUES (%(word)s, %(sentiment)s, %(resource)s, 1,0) 
                                   ON CONFLICT (word, sentiment, resource) DO UPDATE 
                                   SET occurences = words.occurences + 1 
                                   WHERE 1 = 1
                                   AND words.word = %(word)s
                                   AND words.sentiment = %(sentiment)s
                                   AND words.resource = %(resource)s
                                    """

            # executemany() to insert multiple rows rows
            cursor.executemany(sql_insert_query, records)
            self.db.commit()
            print(cursor.rowcount, "Record inserted successfully into mobile table")

        except (Exception, psycopg2.Error) as error:
            self.db.rollback()
            print("Failed inserting record into mobile table {}".format(error))

        finally:
            # closing database self.db.
            if self.db:
                cursor.close()
                self.db.close()
                # print("PostgreSQL self.db is closed")

    def upload_words_values(self, resources: Resources, type):
        try:
            cursor = self.db.cursor()
            records = []

            if type == "posneg":
                records = resources.get_posneg_records()
            elif type == "conscore":
                records = resources.get_conscore_records()

            else:
                print("specifica tipo di risorsa, posneg o conscor")

            sql_insert_query = """ INSERT INTO scores (word, word_value, resource_type, resource_name, occurences) 
                                   VALUES (%(word)s, %(word_value)s, %(resource_type)s, %(resource_name)s, 1) 
                                   ON CONFLICT (word, word_value, resource_type, resource_name) DO UPDATE 
                                   SET occurences = scores.occurences + 1 
                                   WHERE 1 = 1
                                   AND scores.word = %(word)s
                                   AND scores.word_value = %(word_value)s
                                   AND scores.resource_type = %(resource_type)s
                                   AND scores.resource_name = %(resource_name)s
                                   """

            # executemany() to insert multiple rows rows
            cursor.executemany(sql_insert_query, records)
            self.db.commit()
            print(cursor.rowcount, "Record inserted successfully into mobile table")

        except (Exception, psycopg2.Error) as error:
            self.db.rollback()
            print("Failed inserting record into mobile table {}".format(error))

        finally:
            # closing database self.db.
            if self.db:
                cursor.close()
                self.db.close()
                # print("PostgreSQL self.db is closed")

    def upload_tweets(self, tweets: List[TweetData]):
        try:
            cursor = self.db.cursor()

            sql_insert_query = """
                INSERT INTO tweets 
                (text, sentiment, lemmas, hashtags, emoji_pos, emoji_neg,
                emoji_other, emoticon_pos, emoticon_neg)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            tweet_iterator = map(astuple, tweets)

            cursor.executemany(sql_insert_query, tweet_iterator)
            self.db.commit()
            print(cursor.rowcount, "Record inserted successfully into mobile table")

        except (Exception, psycopg2.Error) as error:
            self.db.rollback()
            print("Failed inserting record into mobile table {}".format(error))

        finally:
            # closing database self.db.
            if self.db:
                cursor.close()
                self.db.close()
                print("PostgreSQL self.db is closed")

    def get_filtered_lemmas(self):

        records = None

        try:
            cursor = self.db.cursor()

            sql_insert_query = """
                   SELECT * 
                   FROM tweet_word_frequencies 
                   ORDER BY sentiment, lemma_count DESC;
                   """

            cursor.execute(sql_insert_query)
            records = cursor.fetchall()
            self.db.commit()

        except (Exception, psycopg2.Error) as error:
            self.db.rollback()
            print("Failed selecting record into mobile table {}".format(error))

        finally:
            # closing database self.db.
            if self.db:
                cursor.close()
                self.db.close()

        return records

    def refresh_materialized_view(self):

        cursor = None

        try:
            cursor = self.db.cursor()

            sql_insert_query = """
                   REFRESH MATERIALIZED VIEW tweet_word_frequencies
                   """

            cursor.execute(sql_insert_query)
            self.db.commit()
            print("materialized view refreshed")

        except (Exception, psycopg2.Error) as error:
            self.db.rollback()
            print("refreshing failed".format(error))

        finally:
            # closing database self.db.
            if self.db:
                cursor.close()
                self.db.close()
                print("PostgreSQL self.db is closed")

    def update_frequency_on_resources(self, rows):

        try:
            cursor = self.db.cursor()

            sql_insert_query = """
                   UPDATE words
                   SET tweet_freq = %s
                   WHERE word = %s AND sentiment = %s
                   """

            cursor.executemany(sql_insert_query, rows)
            self.db.commit()
            print(len(rows), "frequencies updated")

        except (Exception, psycopg2.Error) as error:
            self.db.rollback()
            print("update frequency filed".format(error))

        finally:
            # closing database self.db.
            if self.db:
                cursor.close()
                self.db.close()
                # print("PostgreSQL self.db is closed")

    def get_words(self):

        records = []

        try:

            cursor = self.db.cursor()

            sql_insert_query = """
                   SELECT *
                   FROM words
                   """

            cursor.execute(sql_insert_query)
            records = cursor.fetchall()
            self.db.commit()
            print("record seleccted")

        except (Exception, psycopg2.Error) as error:
            self.db.rollback()
            print("select failed".format(error))

        finally:
            # closing database self.db.
            if self.db:
                cursor.close()
                self.db.close()
                print("PostgreSQL self.db is closed")
        return records

    def add_word(self, rows):
        try:
            cursor = self.db.cursor()

            sql_insert_query = """ INSERT INTO words (word, sentiment, resource, occurences, tweet_freq) 
                                   VALUES (%(word)s, %(sentiment)s, 'new', 0, %(tweet_freq)s)
                                   """

            # executemany() to insert multiple rows rows
            cursor.executemany(sql_insert_query, rows)
            self.db.commit()
            print(cursor.rowcount, "new word inserted successfully into mobile table")

        except (Exception, psycopg2.Error) as error:
            self.db.rollback()
            print("Failed inserting record into mobile table {}".format(error))

        finally:
            # closing database self.db.
            if self.db:
                cursor.close()
                self.db.close()
                print("PostgreSQL self.db is closed")