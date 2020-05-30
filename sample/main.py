from sample.dao.get_dao import get_db
from sample.resources.lexical_resources import LexicalResources


def main():

    PATH = "../data/output/modified_lexical_resources/"

    file = LexicalResources(PATH)

    print(file.get_records())
    # postg = get_db("postgres")
    #
    # postg.upload_words(file)


if __name__ == "__main__":
    main()