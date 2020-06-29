import nltk


def nltk_init():
    for corpus in [
        "wordnet",
        "universal_tagset",
        "averaged_perceptron_tagger",
        "stopwords",
        'twitter_samples'
    ]:
        nltk.download(corpus)


if __name__ == "__main__":
    nltk_init()
