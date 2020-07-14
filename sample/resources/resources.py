from pathlib import Path
from collections import defaultdict
import json


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

    def __get_conscore_words__(self, resource):
        f = resource.open()
        words = f.read().splitlines()
        return [word.split()[0] for word in words]

    def get_word_records(self):

        return [
            {
                "word": word,
                "sentiment": sentiment.name,
                "resource": resource.stem,
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
                "resource_name": resource.stem,
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
                "resource_name": resource.stem,
            }
            for type in self.path.iterdir()
            for resource in type.iterdir()
            for word, value in self.__get_scores__(resource).items() if "_" not in word
        ]

    # def count_frequencies(self, word, sentiment):
    #     result = 0
    #
    #     for resource in sentiment.iterdir():
    #         words = self.__get_words__(resource)
    #         result = result + words.count(word)
    #
    #     return result
    #
    # def count_conscore_frequencies(self, word):
    #     d2 = json.load(open("/home/sinopeta/Google_Drive/Pycharm Projects/MAADB/sentiment_analysis/data/input/other/freqs.txt"))
    #     return d2[word]
    #
    # def __create__freq_concore_dict__(self):
    #
    #     path = Path("/home/sinopeta/Google_Drive/Pycharm Projects/MAADB/sentiment_analysis/data/input/numeric_resources/ConScore")
    #     frequencies = defaultdict()
    #
    #     for resource in path.iterdir():
    #         f = resource.open()
    #         words = f.read().splitlines()
    #         for word in words:
    #             if frequencies.get(word.split()[0]):
    #                 value = frequencies[word.split()[0]]
    #                 frequencies.update({word.split()[0]: value + 1})
    #             else:
    #                 frequencies[word.split()[0]] = 1
    #
    #     return frequencies
    #
    # def __write_freq__(self):
    #     freqs = self.__create__freq_concore_dict__()
    #
    #     with open("/home/sinopeta/Google_Drive/Pycharm Projects/MAADB/sentiment_analysis/data/input/other/freqs.txt", 'w') as file:
    #         file.write(json.dumps(freqs))  # use `json.loads` to do the reverse
