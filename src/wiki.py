import wikipedia
from functools import lru_cache


wikipedia.set_lang("en")


class WikiParser:

    @lru_cache(maxsize=1000)
    def get_articles(self, long, lat):
        articles = wikipedia.geosearch(long, lat, results=10, radius=10_000)
        return [wikipedia.page(article).content for article in articles]

    @lru_cache(maxsize=1000)
    def get_summaries(self, long, lat):
        articles = wikipedia.geosearch(long, lat, results=10, radius=10_000)
        return [wikipedia.page(article).summary for article in articles]


if __name__ == "__main__":
    print(WikiParser.get_summaries(50.35515151395933, 14.457822330758399))
