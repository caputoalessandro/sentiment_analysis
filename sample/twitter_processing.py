from sample.processing.twitter_processor import TwitterProcessor
from pathlib import Path


def twitter_processing(directory):

    directory = Path(directory)
    processor = TwitterProcessor()

    for resource in directory.iterdir():
        with resource.open() as file:
            return [
                processor.process_tweet(line, resource.name[11:-8])
                for line in file.read().splitlines()
            ]


if __name__ == "__main__":
    path = "data/input/prova"
    print(twitter_processing(path))