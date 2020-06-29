from sample.create_tables import create_tables
from sample.upload_resources import upload_resources
from sample.twitter_processing import twitter_processing
from sample.dao.get_dao import get_db


def main():

    create_tables()

    upload_resources()

    tweets_path = "/home/sinopeta/Google Drive/Pycharm Projects/MAADB/sentiment_analysis/data/input/prova"
    twitter_list = twitter_processing(tweets_path)

    postgres = get_db("postgres")
    postgres.upload_tweets(twitter_list)


if __name__ == "__main__":
    main()