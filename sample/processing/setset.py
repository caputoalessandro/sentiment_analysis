from sample.processing.emoticon_emoji import *
import emoji


def ideogram_classifier(ide_set):
    ideograms_classified = {}

    if ide_set.intersection(negemoticons):
        ideograms_classified.setdefault("emoticon_neg", []).append(ide_set.intersection(negemoticons))

    elif ide_set.intersection(posemoticons):
        ideograms_classified.setdefault("emoticon_pos", []).append(ide_set.intersection(posemoticons))

    elif ide_set.intersection(EmojiPos):
        ideograms_classified.setdefault("emoji_pos", []).append(ide_set.intersection(EmojiPos))

    elif ide_set.intersection(EmojiNeg):
        ideograms_classified.setdefault("emoji_neg", []).append(ide_set.intersection(EmojiNeg))

    elif ide_set.intersection(OthersEmoji):
        ideograms_classified.setdefault("emoji_other", []).append(ide_set.intersection(OthersEmoji))

    else:
        ideograms_classified.setdefault("emoji_other", []).append(ide_set.intersection(OthersEmoji))
