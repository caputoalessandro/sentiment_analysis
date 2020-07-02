from sample.dao.dao_abc import DAO
from sample.resources.resources import Resources
from sample.processing.twitter_processor import TweetData
from typing import List
from dataclasses import asdict


class MongoDAO(DAO):

    def __init__(self, db):
        self.db = db

    def upload_words(self, resources: Resources):

        db = self.db.maadb_project
        words = db.words
        word_to_insert = resources.get_word_records()
        if words.insert_many(word_to_insert):
            print("Word Documents inserted successfully")
            self.db.close()
        else:
            self.db.close()
            print("INSERIMENTO FALLITO")

    def upload_words_values(self, resources: Resources, type):

        if type == "posneg":
            word_to_insert = resources.get_posneg_records()
        elif type == "conscore":
            word_to_insert = resources.get_conscore_records()
        else:
            print("specifica tipo di risorsa, posneg o conscor")

        db = self.db.maadb_project
        scores = db.scores
        if scores.insert_many(word_to_insert):
            print(type + "Documents inserted successfully")
            self.db.close()
        else:
            self.db.close()
            print("INSERIMENTO FALLITO")

    def upload_tweets(self, tweets: List[TweetData]):
        db = self.db.maadb_project
        tweets_collection = db.tweets
        if tweets_collection.insert_many(map(asdict, tweets)):
            print("Tweets Documents inserted successfully")
            self.db.close()
        else:
            self.db.close()
            print("INSERIMENTO FALLITO")