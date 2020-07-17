import matplotlib.pyplot as plt
from sample.dao.get_dao import get_db
import math
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
    plt.savefig(f"out/{sentiment.lower()}_stats.png")
    return plt.show()


def stats():

    for sentiment in sentiments:
        v = []
        wor = []
        val = []

        db = get_db("mongo")
        freqs = db.get_resources_word_counts(sentiment)

        db = get_db("mongo")
        total = db.count(sentiment)

        for item in freqs:
            v.append((item["value"] / 60000 * 100, item["_id"]))

        v.sort(key=lambda x: x[0])

        for value, word in v:
            if len(val) == 20:
                break
            if value in val:
                continue
            wor.append(word)
            val.append(value)

        make_plot(sentiment, wor, val)

