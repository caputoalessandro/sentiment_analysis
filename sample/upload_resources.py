from sample.dao.get_dao import get_db
from sample.resources.resources import Resources


def upload_resources():

    LEXICAL_RESOURCES = "../data/input/lexical_resources"
    file = Resources(LEXICAL_RESOURCES)
    postg = get_db("postgres")
    postg.upload_words(file)

    CONSCORE_RESOURCES = "../data/input/numeric_resources"
    file = Resources(CONSCORE_RESOURCES)
    postg = get_db("postgres")
    postg.upload_words_values(file, "conscore")

    POSNEG_RESOURCES = "../data/input/sign_resources"
    file = Resources(POSNEG_RESOURCES)
    postg = get_db("postgres")
    postg.upload_words_values(file, "posneg")


if __name__ == "__main__":
    upload_resources()