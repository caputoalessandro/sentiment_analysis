import os
from sample.resources.lexical_resources import LexicalResources


def create_new_lexical_resources():

    RESOURCE_PATH = "../../data/input/lexical_resources"
    NEW_RESOURCE_PATH = "../../data/output/modified_lexical_resources/"
    
    if not os.path.exists(NEW_RESOURCE_PATH):
        os.mkdir(NEW_RESOURCE_PATH)

    file = LexicalResources(RESOURCE_PATH)

    for sentiment in file.get_sentiments():

        if not os.path.exists(NEW_RESOURCE_PATH + sentiment.name):
            os.mkdir(NEW_RESOURCE_PATH + sentiment.name)

        for resource in file.get_resources(sentiment):
            f = open(resource.path, "r")
            words = f.read().splitlines()

            new_f = open(NEW_RESOURCE_PATH + sentiment.name + "/" + resource.name, "w")
            for word in words:
                if "_" not in word:
                    new_f.write(word + "\n")

if __name__ == "__main__":
    create_new_lexical_resources()