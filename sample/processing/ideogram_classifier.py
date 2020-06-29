from sample.processing.emoticon_emoji import *
import emoji


def ideogram_classifier(ideogram):

    if ideogram in negemoticons:
        return "emoticon_neg"

    elif ideogram in posemoticons:
        return "emoticon_pos"

    elif ideogram in EmojiPos:
        return "emoji_pos"

    elif ideogram in EmojiNeg:
        return "emoji_neg"

    elif ideogram in OthersEmoji:
        return "emoji_other"

    else:
        return 0
