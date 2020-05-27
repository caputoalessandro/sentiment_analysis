import os
from sample.resources.resources import Resources


def create_new_file():

    RESOURCE_PATH = "../../data/input/lexical_resources"
    NEW_RESOURCE_PATH = "../../data/output/modified_lexical_resources/"
    
    if not os.path.exists(NEW_RESOURCE_PATH):
        os.mkdir(NEW_RESOURCE_PATH)

    file = Resources(RESOURCE_PATH)

    for sentiment in file.get_sentiments():

        if not os.path.exists(NEW_RESOURCE_PATH + sentiment):
            os.mkdir(NEW_RESOURCE_PATH + sentiment)

        for resource in file.get_resources(sentiment):
            resources = file.path + '/' + sentiment + '/' + resource
            f = open(resources, "r")
            words = f.read().splitlines()

            new_f = open(NEW_RESOURCE_PATH + sentiment + "/" + resource, "w")
            for word in words:
                if "_" not in word:
                    new_f.write(word + "\n")

