from sample.processing.twitter_processor import TwitterProcessor, TweetData
from pathlib import Path
from sample.processing.nltk_init import nltk_init


def twitter_processing(twitters_path):

    twitters = Path(twitters_path)
    processor = TwitterProcessor()

    with twitters.open() as file:
        for line in file:
            tweet = processor.process_tweet(line, twitters.name[11:-8])
            breakpoint()


if __name__ == "__main__":
    # nltk_init()
    path = "data/input/messages/prova.txt"
    twitter_processing(path)