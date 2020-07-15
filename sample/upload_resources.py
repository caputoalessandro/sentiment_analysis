from sample.dao.get_dao import get_db
from sample.resources.resources import Resources


LEXICAL_RESOURCES = "../data/input/lexical_resources"
CONSCORE_RESOURCES = "../data/input/numeric_resources"
POSNEG_RESOURCES = "../data/input/sign_resources"

lexical_resources = Resources(LEXICAL_RESOURCES)
conscore_resources = Resources(CONSCORE_RESOURCES)
posneg_resources = Resources(POSNEG_RESOURCES)

POTGRES = "postgres"
MONGO = "mongo"

CONSCORE = "conscore"
POSNEG = "posneg"


def postgres_upload_resources():

    postg = get_db(POTGRES)
    postg.upload_words(lexical_resources)

    # postg = get_db(POTGRES)
    # postg.upload_words_values(conscore_resources, CONSCORE)
    #
    # postg = get_db(POTGRES)
    # postg.upload_words_values(posneg_resources, POSNEG)


def mongo_upload_resources():

    mongo = get_db(MONGO)
    mongo.upload_words(lexical_resources)

    mongo = get_db(MONGO)
    mongo.upload_words_values(posneg_resources, POSNEG)

    mongo = get_db(MONGO)
    mongo.upload_words_values(conscore_resources, CONSCORE)


if __name__ == "__main__":
    mongo_upload_resources()