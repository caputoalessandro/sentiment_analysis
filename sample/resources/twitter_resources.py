import os


class twitter_resources:

    def __init__(self,path):
        self.path = path

    def get_sentiments(self):
        sentimets = os.scandir(self.path)
        return [ sentiment for sentiment in sentimets]

    def get_twitters(self, sentiment):
        f = open(sentiment.path, "r")
        twitters = f.read().splitlines()
        return [twitter for twitter in twitters]

    def get_records(self):

        return[
            {
                "sentiment": sentiment.name[11:-8],
                "text": twitter
            }
            for sentiment in self.get_sentiments()
            for twitter in self.get_twitters(sentiment)
        ]


if __name__ == "__main__":
    TWITTER_PATH = "../../data/input/messages"
    t = twitter_resources(TWITTER_PATH)
    print(t.get_records())