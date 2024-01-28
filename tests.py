from gnews import GNews

google_news = GNews()
australia_news = google_news.get_news('australia news')

# Iterate through the news articles and print the titles
for article in australia_news:
    print(article['title'])