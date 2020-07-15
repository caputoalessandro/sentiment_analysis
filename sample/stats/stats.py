from sample.dao.get_dao import get_db
import matplotlib.pyplot as plt


def make_plot(sentiment, words, values):
    plt.figure(figsize=(25, 12))
    plt.subplot(132)
    plt.bar(words, values)
    plt.suptitle(sentiment)
    plt.show()


def postgres_calculate_percentage():
    db = get_db("postgres")
    twitter_lemmas = db.get_filtered_lemmas()

    db = get_db("postgres")
    resources_words = db.get_words()

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

    lemmas_number = {
        sentiment: len([
            row for row in twitter_lemmas if row[0] == sentiment
        ])
        for sentiment, word, freq in twitter_lemmas
    }

    stats = {

        sentiment: sorted(
            [
                (word, (tweet_freq / lemmas_number[sentiment]) * 100)
                for word, s, resource, res_freq, tweet_freq in resources_words if s == sentiment
            ],
            key=lambda tup: tup[1],
            reverse=True)

        for sentiment in sentiments
    }

    w = []
    v = []

    for sentiment, words in stats.items():
        for word, value in words[:5]:
            w.append(word)
            v.append(value)
        make_plot(sentiment, w, v)

    return 0

