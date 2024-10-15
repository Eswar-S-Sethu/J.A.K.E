from gnews import GNews

# Initialize GNews with the desired language and country
gnews = GNews(language='en', country='AU')

# Fetch the top news articles
top_news = gnews.get_top_news()

# Prepare a list for the headlines and summaries
summaries = []

# Get the first 5 articles
for article in top_news[:5]:
    summaries.append({
        'headline': article['title'],
        'summary': article['description']
    })

# Print the summaries
for i, item in enumerate(summaries, 1):
    print(f"Article {i}:")
    print(f"Headline: {item['headline']}")
    print(f"Summary: {item['summary']}")
    print()
