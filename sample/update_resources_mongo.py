from sample.dao.get_dao import get_db

DB = "mongo"


def update_resources_mongo():

    db = get_db(DB)
    twitter_lemmas = db.get_tweets()

    db = get_db(DB)
    resources_words = db.get_words()

    update = []

    for twitter_sentiment, twitter_words in twitter_lemmas.items():

        for twitter_item in twitter_words:

            twitter_word_in_resources = [item for item in resources_words
                            if twitter_item["_id"] == item["word"]
                            and twitter_sentiment == item["sentiment"]]

            update = {
                "word": twitter_item["_id"],
                "sentiment":  twitter_sentiment,
                "resource":  "new",
                "tweet_freq": twitter_item["value"]
            }

            if twitter_word_in_resources:
                db = get_db(DB)
                db.update_frequency_on_resources(update)

            elif not twitter_word_in_resources and twitter_item["value"] > 1:

                db = get_db(DB)
                db.add_word(update)

    return 0



