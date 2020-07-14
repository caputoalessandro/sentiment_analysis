from sample.dao.get_dao import get_db
from collections import Counter


def update_resources(DB):

    db = get_db(DB)
    twitter_lemmas = db.get_filtered_lemmas()

    db = get_db(DB)
    resources_words = db.get_words()

    update = []
    add = []

    for sentiment, word, freq in twitter_lemmas:

        twitters_lemmas_counts = {x[1]: x[2] for x in twitter_lemmas if x[0] == sentiment}

        if [item for item in resources_words if word == item[0] and sentiment == item[1]]:
            update.append((
                twitters_lemmas_counts[word],
                word,
                sentiment
            ))

        if word not in resources_words:

            add.append({
                "word": word,
                "sentiment": sentiment,
                "tweet_freq": twitters_lemmas_counts[word]
            })

        db = get_db(DB)
        db.update_frequency_on_resources(update)

        db = get_db(DB)
        db.add_word(add)

