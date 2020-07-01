from sample.processing.twitter_processor import TwitterProcessor
from pathlib import Path


def process_tweets(directory="/home/sinopeta/Google Drive/Pycharm Projects/MAADB/sentiment_analysis/data/input/prova"):

    directory = Path(directory)
    processor = TwitterProcessor()

    for resource in directory.iterdir():
        with resource.open() as file:
            return [
                processor.process_tweet(line, resource.name[11:-8])
                for line in file.read().splitlines()
            ]
