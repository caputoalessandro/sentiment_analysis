from sample.create_tables import create_tables
from sample.upload_resources import postgres_upload_resources,mongo_upload_resources
from sample.process_tweets import process_tweets
from sample.dao.get_dao import get_db
from sample.word_clouds import make_all_word_clouds


POSTGRES = "postgres"
MONGO_DB = "mongo"


def main():

    # processed_tweets = process_tweets()

    # create_tables()
    # postgres_upload_resources()
    #
    # pg = get_db(POSTGRES)
    # pg.upload_tweets(processed_tweets)
    #
    # pg = get_db(POSTGRES)
    # pg.refresh_materialized_view()

    pg = get_db(POSTGRES)
    postgres_filtered = pg.get_filtered_frequencies()

    make_all_word_clouds(postgres_filtered, POSTGRES)

    # mongo = get_db(MONGO_DB)
    # mongo_upload_resources()

    # mongo = get_db(MONGO_DB)
    # mongo.upload_tweets(processed_tweets)

    # mongo = get_db(MONGO_DB)
    # mongo.count_tweet_lemmas_frequencies()

    # mongo = get_db(MONGO_DB)
    # mongo_filtered = mongo.get_filtered_frequencies()
    # breakpoint()
    # make_all_word_clouds(mongo_filtered, MONGO_DB)


if __name__ == "__main__":
    main()