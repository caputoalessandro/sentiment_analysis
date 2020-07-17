from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def make_wordcloud(words, sentiment):

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          min_font_size=10).generate_from_frequencies(words)

    # plot the WordCloud image
    plt.figure(figsize=(8, 9), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.suptitle(sentiment, fontsize=30)
    plt.savefig(f"out/{sentiment.lower()}_wordcloud.png")
    plt.show()

