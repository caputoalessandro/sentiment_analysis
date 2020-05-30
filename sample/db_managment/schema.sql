DROP TABLE IF EXISTS words;
CREATE TABLE words (
    word varchar,
    sentiment varchar,
    resource varchar,
    occurences int,
    PRIMARY KEY (word, sentiment, resource)
)

DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets (
    id SERIAL PRIMARY KEY,
    text VARCHAR,
    sentiment VARCHAR,
    lemmas VARCHAR [],
    hashtags VARCHAR [],
    emoji_pos VARCHAR [],
    emoji_neg VARCHAR [],
    emoji_other VARCHAR [],
    emoticon_pos VARCHAR [],
    emoticon_neg VARCHAR []
);