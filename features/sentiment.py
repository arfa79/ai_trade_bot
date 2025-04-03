from transformers import pipeline
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_news(query="Bitcoin"):
    """Scrape news headlines using NewsAPI."""
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={os.getenv('NEWS_API_KEY')}"
    response = requests.get(url)
    return [article['title'] for article in response.json()['articles'][:5]]

def analyze_sentiment(texts):
    """Classify sentiment using FinBERT."""
    finbert = pipeline("text-classification", model="yiyanghkust/finbert-tone")
    return finbert(texts)

# Example usage:
# news = fetch_news()
# sentiments = analyze_sentiment(news)