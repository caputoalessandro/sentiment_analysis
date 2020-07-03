from sample.create_tables import create_tables
from sample.upload_resources import postgres_upload_resources,mongo_upload_resources
from sample.process_tweets import process_tweets
from sample.dao.get_dao import get_db

POSTGRES = "postgres"
MONGO_DB = "mongo"


def main():

    processed_tweets = process_tweets()

    # create_tables()
    #
    # postgres_upload_resources()

    # pg = get_db(POSTGRES)
    # pg.upload_tweets(processed_tweets)
    #
    # mongo_upload_resources()
    #
    mongo = get_db(MONGO_DB)
    # mongo.upload_tweets(processed_tweets)

    result = mongo.count_tweet_lemmas_frequencies("anger")


if __name__ == "__main__":
    main()