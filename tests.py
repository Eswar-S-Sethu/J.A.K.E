from gnews import GNews
from newspaper import Article
google_news = GNews(language="en",max_results=5)
news = google_news.get_news_by_site("bbc.com")
newsData={}
print(news[1]["url"])