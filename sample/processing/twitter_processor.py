from nltk.corpus import stopwords
from nltk.corpus.reader import wordnet
from nltk.tag import PerceptronTagger
from nltk.tokenize.casual import TweetTokenizer
from dataclasses import dataclass, field, asdict
from typing import List
from sample.processing.ideogram_classifier import ideogram_classifier
from sample.processing.slang_to_tokens import slang_to_tokens_map
from nltk.stem import PorterStemmer
import emot
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
    themes: List[str]
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
        self.stemmer = PorterStemmer()
        self.slang_to_tokens = slang_to_tokens_map()


    def process_tweet(self, message, sentiment):

        hashtags = []
        themes = []

        # tokens = message.split()
        tokens = self.tokenizer.tokenize(message)
        tokens = self._expand_slang(tokens)
        tagged_tokens = self.tagger.tag(tokens)
        # breakpoint()
        stemmer = self.stemmer

        ideograms = self._find_ideograms(message)

        for token, pos in tagged_tokens:

            if token in STOPWORDS:
                continue

            elif HASHTAG_RE.fullmatch(token):
                hashtags.append(token)

            elif pos[0] in TAGS_CONVERSIONS:
                theme = stemmer.stem(token)
                if theme in STOPWORDS or not WORD_RE.fullmatch(theme):
                    continue
                themes.append(theme)

        return TweetData(
            message, sentiment, themes, hashtags, **ideograms
        )

    def _find_ideograms(self, message):
        emojis_dict = {}
        emoticon_dict = {}

        emojis = emot.emoji(message)

        if emojis:
            for ideogram in emojis["value"]:
                classification = ideogram_classifier(ideogram)
                if classification:
                    emojis_dict.setdefault(classification, []).append(ideogram)

        for token in message.split():
            classification = ideogram_classifier(token)
            if classification:
                emoticon_dict.setdefault(classification, []).append(token)

        return dict(emoticon_dict, **emojis_dict)


    def _expand_slang(self, tokens):
        slang_to_tokens = self.slang_to_tokens

        result = []
        for token in tokens:
            result.extend(slang_to_tokens.get(token, (token,)))

        return result

