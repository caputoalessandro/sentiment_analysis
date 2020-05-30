import os


class LexicalResources:

    def __init__(self, path):
        self.path = path

    def get_sentiments(self):
        sentiments = os.scandir(self.path)
        return [sentiment for sentiment in sentiments]

    def get_resources(self, sentiment):
        resources = os.scandir(sentiment.path)
        return [resource for resource in resources]

    def get_words(self, resource):
        f = open(resource.path, "r")
        words = f.read().splitlines()
        return [word for word in words]

    def get_records(self):

        return [
            {
                "word": word,
                "sentiment": sentiment.name,
                "resource": resource.name[:-4]
            }
            for sentiment in self.get_sentiments()
            for resource in self.get_resources(sentiment)
            for word in self.get_words(resource)
        ]


if __name__ == "__main__":
    PATH = "../data/output/modified_lexical_resources/"
    file = LexicalResources(PATH)
