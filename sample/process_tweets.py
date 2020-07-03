from sample.processing.twitter_processor import TwitterProcessor
from pathlib import Path


def process_tweets(directory="/home/sinopeta/Google_Drive/Pycharm Projects/MAADB/sentiment_analysis/data/input/messages/dataset_dt_anger_60k.txt"):

    directory = Path(directory)
    processor = TwitterProcessor()

    # for resource in directory.iterdir():
    with directory.open() as file:
        return [
            processor.process_tweet(line, directory.name[11:-8])
            for line in file.read().splitlines()
        ]
