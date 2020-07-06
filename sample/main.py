from sample.create_tables import create_tables
from sample.upload_resources import postgres_upload_resources,mongo_upload_resources
from sample.process_tweets import process_tweets
from sample.dao.get_dao import get_db
from sample.word_cloud.word_cloud import make_wordcloud


POSTGRES = "postgres"
MONGO_DB = "mongo"


def main():

    # processed_tweets = process_tweets()

    # create_tables()
    pg = get_db(POSTGRES)
    # postgres_upload_resources()
    # pg.upload_tweets(processed_tweets)
    # pg.refresh_materialized_view()
    postgres_filtered = pg.get_filtered_frequencies()

    mongo = get_db(MONGO_DB)
    # mongo_upload_resources()
    # mongo.upload_tweets(processed_tweets)
    # mongo.count_tweet_lemmas_frequencies()
    mongo_filtered = mongo.get_filtered_frequencies()

    words = {
        word["_id"]: word["value"]
        for word in mongo_filtered["anger"]
    }

    make_wordcloud(words)


if __name__ == "__main__":
    main()