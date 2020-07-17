from sample.processing.twitter_processor import TwitterProcessor
from pathlib import Path,PurePath


def process_tweets(directory="/home/sinopeta/Google_Drive/Pycharm Projects/MAADB/sentiment_analysis/data/input/messages"):

    directory = Path(directory)
    processor = TwitterProcessor()
    result = []

    for sentiment in directory.iterdir():
        with sentiment.open() as file:
            tweets = [
                processor.process_tweet(line, PurePath(sentiment).name[11:-8])
                for line in file.read().splitlines()
            ]

        result = result + tweets

    return result