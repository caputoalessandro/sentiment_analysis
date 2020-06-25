from nltk.corpus import stopwords
from nltk.corpus.reader import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tag import PerceptronTagger
from nltk.tokenize.casual import TweetTokenizer
from dataclasses import dataclass, field, asdict
from typing import List
import re


STOPWORDS = set(stopwords.words("english"))
STOPWORDS.add("USERNAME")
STOPWORDS.add("URL")
STOPWORDS.update(["i'm", "get", "know", "go"])

TAGS_CONVERSIONS = {
    "J": wordnet.ADJ,
    "V": wordnet.VERB,
    "N": wordnet.NOUN,
    "R": wordnet.ADV,
}

HASHTAG_RE = re.compile(r"#\w*[A-Za-z]+\w*")
WORD_RE = re.compile(r"['\w]+")


@dataclass
class TweetData:
    text: str
    sentiment: str
    lemmas: List[str]
    hashtags: List[str]
    emoji_pos: List[str] = field(default_factory=list)
    emoji_neg: List[str] = field(default_factory=list)
    emoji_other: List[str] = field(default_factory=list)
    emoticon_pos: List[str] = field(default_factory=list)
    emoticon_neg: List[str] = field(default_factory=list)


class TwitterProcessor:

    def __init__(self):
        self.tagger = PerceptronTagger()
        self.tokenizer = TweetTokenizer()
        self.lemmatizer = WordNetLemmatizer()
        # self.ideogram_classifier = get_ideogram_classifier()
        # self.slang_to_tokens_map = get_slang_to_tokens_map()

    def process_tweet(self, message):

        hashtags = []

        tokens = self.tokenizer.tokenize(message)
        tagged_tokens = self.tagger.tag(tokens)

        for token, pos in tagged_tokens:

            if token in STOPWORDS:
                continue

            elif HASHTAG_RE.fullmatch(token):
                hashtags.append(token)