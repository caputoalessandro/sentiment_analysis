DROP TABLE IF EXISTS words;
CREATE TABLE words (
--     id  SERIAL PRIMARY KEY,
    word varchar,
    sentiment varchar,
    resource varchar,
    occurences int,
    tweet_freq int,
    PRIMARY KEY (word, sentiment, resource)
);


DROP TABLE IF EXISTS scores;
CREATE TABLE  scores (
--     id  SERIAL PRIMARY KEY,
    word varchar,
    word_value varchar,
    resource_type varchar,
    resource_name varchar,
    occurences int,
    PRIMARY KEY (word, word_value, resource_type , resource_name)
);


DROP TABLE IF EXISTS tweets CASCADE;
CREATE TABLE tweets  (
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



DROP MATERIALIZED VIEW IF EXISTS tweet_word_frequencies;
CREATE MATERIALIZED VIEW tweet_word_frequencies
AS
    SELECT sentiment, lemma, COUNT(lemma) as lemma_count
    FROM tweets, LATERAL unnest(lemmas) as lemma
    GROUP BY sentiment, lemma
    ORDER BY lemma_count DESC
WITH NO DATA ;

-- REFRESH MATERIALIZED VIEW tweet_word_frequencies;