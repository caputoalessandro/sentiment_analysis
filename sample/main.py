from sample.create_tables import create_tables
from sample.upload_resources import postgres_upload_resources,mongo_upload_resources
from sample.process_tweets import process_tweets
from sample.dao.get_dao import get_db

POSTGRES = "postgres"
MONGO_DB = "mongo"


def main():

    create_tables()

    postgres_upload_resources()

    mongo_upload_resources()

    processed_tweets = process_tweets()

    pg = get_db(POSTGRES)
    pg.upload_tweets(processed_tweets)

    mongo = get_db(MONGO_DB)
    mongo.upload_tweets(processed_tweets)


if __name__ == "__main__":
    main()