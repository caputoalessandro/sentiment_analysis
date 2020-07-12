from sample.word_cloud.word_cloud import make_wordcloud
from collections import defaultdict
from itertools import islice


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


def make_all_word_clouds(filtered_words, db):

    if db == "mongo":

        result = {
            key:
                {
                word["_id"]: word["value"]
                for word in filtered_words[key]
            }
            for key in filtered_words
        }

    elif db == "postgres":

        words = defaultdict(dict)
        result = defaultdict(dict)

        for sentiment, word, value in filtered_words:
            words[sentiment][word] = value

        for sentiment, lemmas in words.items():
            rows = take(40, lemmas.items())
            result[sentiment] = dict(rows)

    for sentiment in result:
        make_wordcloud(result[sentiment])



if __name__ == "__main__":
    make_all_word_clouds()