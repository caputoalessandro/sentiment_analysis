from sample.dao.get_dao import get_db
import matplotlib.pyplot as plt
import numpy as np

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


def make_plot(sentiment, words, values):

    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    y_pos = np.arange(len(words))

    ax.barh(y_pos, values, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Percentage %')
    ax.set_title(sentiment)

    plt.show()


def mongo_calculate_percentage(n):
    db = get_db("mongo")
    twitter_lemmas = db.get_filtered_lemmas()

    db = get_db("mongo")
    resources_words = db.get_words()

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

    for sentiment, words in stats.items():
        w = []
        v = []

        for word, value in words[:n]:
            w.append(word)
            v.append(value)

        make_plot(sentiment, w, v)

    return 0


def mongo_calculate_percentage():
    db = get_db("mongo")
    twitter_lemmas = db.get_filtered_lemmas()

    db = get_db("mongo")
    resources_words = db.get_words()

    breakpoint()