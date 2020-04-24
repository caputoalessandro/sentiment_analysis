import os


class Resources:

    path = str

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

    def create_new_resources(self, new_resource):

        if not os.path.exists(new_resource):
            os.mkdir(new_resource)

        for sentiment in self.get_sentiments():
            if not os.path.exists(new_resource + sentiment):
                os.mkdir(new_resource + sentiment)

            for resource in self.get_resources(sentiment):
                resource_path = self.path + '/' + sentiment + '/' + resource
                f = open(resource_path, "r")
                words = f.read().splitlines()

                new_f = open(new_resource + sentiment + "/" + resource, "w")
                for word in words:
                    if "_" not in word:
                        new_f.write(word + "\n")