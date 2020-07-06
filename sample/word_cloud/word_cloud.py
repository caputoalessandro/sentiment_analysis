from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict,List


def make_wordcloud(words):

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          min_font_size=10).generate_from_frequencies(words)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.show()
