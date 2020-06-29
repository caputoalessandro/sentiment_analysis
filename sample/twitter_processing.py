from sample.processing.twitter_processor import TwitterProcessor, TweetData
from pathlib import Path
from sample.processing.nltk_init import nltk_init


def twitter_processing(twitters_path):

    twitters = Path(twitters_path)
    processor = TwitterProcessor()

    with twitters.open() as file:
        for line in file.read().splitlines():
            tweet = processor.process_tweet(line, twitters.name[11:-8])


if __name__ == "__main__":
    # nltk_init()
    path = "data/input/messages/dataset_dt_anger_60k.txt"
    twitter_processing(path)