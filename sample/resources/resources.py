from pathlib import Path


class LexicalResources:

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

    def get_lexical_resources_records(self):

        return [
            {
                "word": word,
                "value": sentiment.name,
                "resource": resource.stem
            }
            for sentiment in self.path.iterdir()
            for resource in sentiment.iterdir()
            for word in self.__get_words__(resource) if "_" not in word
        ]

    def get_conscore_resources_records(self):

        return [
            {
                "word": word,
                "value": value,
                "type": type.name,
                "resource": resource.stem
            }
            for type in self.path.iterdir()
            for resource in type.iterdir()
            for word, value in self.__get_scores__(resource).items() if "_" not in word
        ]


if __name__ == "__main__":
    PATH = "../../data/input/numeric_resources"
    file = LexicalResources(PATH)
    print(file.get_conscore_resources_records())