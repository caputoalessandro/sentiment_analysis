from abc import ABC, abstractmethod
from sample.resources.resources import Resources
from sample.processing.twitter_processor import TweetData
from typing import List


class DAO(ABC):

    @abstractmethod
    def upload_words(self, resources: Resources):
        pass

    @abstractmethod
    def upload_words_values(self, resources: Resources, type):
        pass

    @abstractmethod
    def upload_tweets(self, tweets: List[TweetData]):
        pass

    @abstractmethod
    def count_tweet_lemmas_frequencies(self, sentiment):
        pass


