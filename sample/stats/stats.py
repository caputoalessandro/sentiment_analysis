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

INF = 600000000


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

    return plt.show()


def make_plots(stats: dict, n):

    w = []
    v = []

    for sentiment, words in stats.items():
        w.clear()
        v.clear()

        for word, value in words[:n]:
            w.append(word)
            v.append(value)

        make_plot(sentiment, w, v)

    return 0


def postgres_calculate_percentage(n):
    db = get_db("postgres")
    twitter_lemmas = db.get_filtered_lemmas()

    db = get_db("postgres")
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

    return make_plots(stats, n)


def mongo_calculate_percentage(n):
    db = get_db("mongo")
    twitter_lemmas = db.get_filtered_lemmas(INF)

    db = get_db("mongo")
    resources_words = db.get_words()

    stats = {}

    for sentiment in sentiments:
        for row in resources_words:
            if "tweet_freq" not in row:
                continue
            elif "tweet_freq" in row and sentiment == row["sentiment"]:
                stats.setdefault(sentiment, [])
                stats[sentiment].append(
                    (row["word"], row["tweet_freq"] / len(twitter_lemmas[sentiment]) * 100)
                )

    return make_plots(stats, n)


