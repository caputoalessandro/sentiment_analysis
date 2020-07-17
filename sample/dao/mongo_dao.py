from sample.dao.dao_abc import DAO
from sample.resources.resources import Resources
from sample.processing.twitter_processor import TweetData
from typing import List
from dataclasses import asdict
from bson.code import Code


class MongoDAO(DAO):

    def __init__(self, db):
        self.sentiments = [
            "anger",
            "anticipation",
            "disgust",
            "fear",
            "joy",
            "sadness",
            "surprise",
            "trust"
        ]
        self.db = db

    def upload_words(self, resources: Resources):

        db = self.db.maadb_project
        words = db.words
        words.drop()
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
        scores.drop()
        if scores.insert_many(word_to_insert):
            print(type + "Documents inserted successfully")
            self.db.close()
        else:
            self.db.close()
            print("INSERIMENTO FALLITO")

    def upload_tweets(self, tweets: List[TweetData]):
        db = self.db.maadb_project
        tweets_collection = db.tweets
        tweets_collection.drop()
        if tweets_collection.insert_many(map(asdict, tweets)):
            print("Tweets Documents inserted successfully")
            self.db.close()
        else:
            self.db.close()
            print("INSERIMENTO FALLITO")

    def count_tweet_lemmas_frequencies(self):

        for sentiment in self.sentiments:
            self._map_reduce(sentiment)
        self.db.close()
        return 0

    def _map_reduce(self, sentiment):

        map = Code("""
                   function () {
                     this.themes.forEach(function(z) {
                       emit(z, 1);
                     });
                   }
                   """)

        reduce = Code("""
                      function (key, values) {
                          var total = 0;
                          for (var i = 0; i < values.length; i++) {
                              total += values[i];
                          }
                          return total;
                      }"""
                      )

        self.db.maadb_project[f"{sentiment}_freqs"].drop()
        print(sentiment, "words frequencies calculated")

        res = self.db.maadb_project.tweets.map_reduce(
            map,
            reduce,
            f"{sentiment}_freqs",
            query={"sentiment": sentiment})

        self.db.close()

        return res

    def get_filtered_lemmas(self,n):
        frequencies = {}
        for sentiment in self.sentiments:
            collection = self.db.maadb_project[f"{sentiment}_freqs"]
            aggregate = collection.find({}).sort('value', -1).limit(n)
            frequencies.setdefault(sentiment)
            frequencies[sentiment] = list(aggregate)
        self.db.close()
        return frequencies

    def update_frequency_on_resources(self, row):

        collection = self.db.maadb_project[f"{row['sentiment']}_freqs"]
        query = {"word": row["word"], "sentiment": row["sentiment"]}
        values = {"$set": {"tweet_freq": row["tweet_freq"]}}
        if not collection.update_one(query, values):
            print("UPDATE FAILED")
            self.db.close()
        print("frequency updated")
        self.db.close()

    def add_word(self, rows):
        collection = self.db.maadb_project.words
        if collection.insert_many(rows):
            print(len(rows),"Word Documents inserted successfully")
            self.db.close()
        else:
            self.db.close()
            print("INSERIMENTO FALLITO")

    def get_words(self):
        collection = self.db.maadb_project.words
        res = list(collection.find({}))
        self.db.close()
        return res

    def get_tweets(self):
        frequencies = {}
        for sentiment in self.sentiments:
            collection = self.db.maadb_project[f"{sentiment}_freqs"]
            aggregate = collection.find({}).sort('value', -1)
            frequencies.setdefault(sentiment)
            frequencies[sentiment] = list(aggregate)
        self.db.close()
        return frequencies

    def get_emojis(self):
        collection = self.db.maadb_project.tweets
        res = list(collection.find({}, {"emoji_pos": 1}))
        self.db.close()
        return res

    def get_emoticons(self):
        collection = self.db.maadb_project.tweets
        res = list(collection.find({}).projection({"emoticon_pos": 1, "emoticon_neg": 1, "_id": 0}))
        self.db.close()
        return res

    def tweet_word_freqs(self, sentiment):
        words = list(self.db.maadb_project.words.find({"sentiment": sentiment}))
        words = [word["word"] for word in words]
        freqs = (
                list(self.db.maadb_project[f"{sentiment}_freqs"]
                .find({"_id": {"$in": words}}))

        )
        res = list(freqs)
        self.db.close()
        return res

    def get_resources_word_counts(self, sentiment: str):
        words = list(self.db.maadb_project.words.find({"sentiment": sentiment}))
        words = [word["word"] for word in words]
        freqs = (
            list(self.db.maadb_project[f"{sentiment}_freqs"]
            .find({"_id": {"$in": words}}))
        )

        return freqs

    def count(self, sentiment):
        return self.db.maadb_project[f"{sentiment}_freqs"].count()
