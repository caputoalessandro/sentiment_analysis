DROP TABLE IF EXISTS words;
CREATE TABLE words (
    word varchar,
    sentiment varchar,
    resource varchar,
    occurences int,
    PRIMARY KEY (word, sentiment, resource)
)