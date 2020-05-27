import os


class Resources:

    def __init__(self, path):
        self.path = path

    def get_sentiments(self):
        sentiments = os.scandir(self.path)
        return [sentiment.name for sentiment in sentiments]

    def get_resources(self, sentiment):
        resources = os.scandir(self.path + '/' + sentiment)
        return [resource.name for resource in resources]

    def get_words(self, sentiment, resource):
        resource = self.path + '/' + sentiment + '/' + resource
        f = open(resource, "r")
        words = f.read().splitlines()
        return [word for word in words]

    def count_word_occurrence(self, sentiment, resource, word):
        words = self.get_words(sentiment, resource)
        return words.count(word)

    def count_word_percentage(self, sentiment, resource, word):
        number_of_words = len(self.get_words(sentiment, resource))
        word_occurrence = self.count_word_occurrence(sentiment, resource, word)
        return word_occurrence / number_of_words * 100
