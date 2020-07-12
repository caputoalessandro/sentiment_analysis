from pathlib import Path


class Resources:

    def __init__(self, path):
        self.path = Path(path)

    def __get_words__(self, resource):
        f = open(resource, "r")
        words = f.read().splitlines()
        return [word for word in words]

    def __get_scores__(self, resource):
        f = open(resource, "r")
        words = f.read().splitlines()
        return { word.split()[0]: word.split()[1] for word in words}

    def get_word_records(self):

        return [
            {
                "word": word,
                "sentiment": sentiment.name,
                "resource": resource.stem,
                "occurences": self.count_frequencies(word,sentiment)
            }
            for sentiment in self.path.iterdir()
            for resource in sentiment.iterdir()
            for word in self.__get_words__(resource) if "_" not in word
        ]

    def get_posneg_records(self):

        return [
            {
                "word": word,
                "word_value": sign.name,
                "resource_type": "posneg",
                "resource_name": resource.stem
            }
            for sign in self.path.iterdir()
            for resource in sign.iterdir()
            for word in self.__get_words__(resource) if "_" not in word
        ]

    def get_conscore_records(self):

        return [
            {
                "word": word,
                "word_value": value,
                "resource_type": type.name,
                "resource_name": resource.stem
            }
            for type in self.path.iterdir()
            for resource in type.iterdir()
            for word, value in self.__get_scores__(resource).items() if "_" not in word
        ]

    def count_frequencies(self, word, sentiment):
        result = 0


        for resource in sentiment.iterdir():
            words = self.__get_words__(resource)
            result = result + words.count(word)

        return result