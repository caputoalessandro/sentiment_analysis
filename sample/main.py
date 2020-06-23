from sample.dao.get_dao import get_db
from sample.resources.lexical_resources import LexicalResources
from sample.db_managment.create_tables import create_tables


def main():

    SCHEMA = '/home/sinopeta/PyCharm-Projects/MAADB/sentiment_analysis/sample/db_managment/schema.sql'
    create_tables(SCHEMA)

    PATH = "/home/sinopeta/PyCharm-Projects/MAADB/sentiment_analysis/data/input/lexical_resources"
    file = LexicalResources(PATH)

    postg = get_db("postgres")
    postg.upload_words(file)


if __name__ == "__main__":
    main()