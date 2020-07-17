from sample.create_tables import create_tables
from sample.upload_resources import postgres_upload_resources, mongo_upload_resources
from sample.process_tweets import process_tweets
from sample.dao.get_dao import get_db
from sample.word_clouds import make_all_word_clouds
from sample.add_new_words import add_new_words
from sample.stats.stats import stats


POSTGRES = "postgres"
MONGO_DB = "mongo"


def main():

    # """ Process tweets """
    # processed_tweets = process_tweets()
    #
    # """ Upload resources on Postgres """
    # create_tables()
    # postgres_upload_resources()
    #
    # pg = get_db(POSTGRES)
    # pg.upload_tweets(processed_tweets)
    #
    # pg = get_db(POSTGRES)
    # pg.refresh_materialized_view()
    #
    # """ Upload resources on Mongo DB """
    # mongo_upload_resources()
    #
    # mongo = get_db(MONGO_DB)
    # mongo.upload_tweets(processed_tweets)
    #
    # mongo = get_db(MONGO_DB)
    # mongo.count_tweet_lemmas_frequencies()
    #
    # """Add new words postgres """
    # add_new_words(POSTGRES)
    #
    # """Add new word mongo"""
    # add_new_words(MONGO_DB)

    """ Make wordclouds on postgres """
    # pg = get_db(POSTGRES)
    # postgres_filtered = pg.get_filtered_lemmas(50)
    # make_all_word_clouds(postgres_filtered, POSTGRES)

    """ Make word clouds on Mongo DB """
    # mongo = get_db(MONGO_DB)
    # mongo_filtered = mongo.get_filtered_lemmas(60)
    # make_all_word_clouds(mongo_filtered, MONGO_DB)

    """ Make Stats """
    stats()

    return 0


if __name__ == "__main__":
    main()