from sample.dao.get_dao import get_db

sentiments = [
    "anger",
    "anticipation",
    "disgust",
    "fear",
    "joy",
    "sadness",
    "surprise",
    "trust"
]


def add_new_words(DB):

    rows = []

    for sentiment in sentiments:

        db = get_db(DB)
        words = db.tweet_word_freqs(sentiment)
        for word, freq in words[:5]:

            w = {
                'word': word,
                'sentiment': sentiment,
                'freq': freq
            }

            rows.append(w)

    db = get_db(DB)
    db.add_word(rows)