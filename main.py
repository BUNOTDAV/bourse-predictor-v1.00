import requests
import pandas as pd
from textblob import TextBlob
from bs4 import BeautifulSoup

# CONFIG
NEWS_API_KEY = '8e16ef1c93a04a529617e389097ec3ea'
FINNHUB_API_KEY = 'YOUR_FINNHUB_API_KEY'
STOCKS = ['AAPL', 'MSFT', 'GOOGL', 'BNP.PA', 'AIR.PA']

def get_newsapi_news(stock):
    url = f'https://newsapi.org/v2/everything?q={stock}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return [article['title'] for article in data.get('articles', [])[:5]]

def get_finnhub_news(stock):
    url = f'https://finnhub.io/api/v1/company-news?symbol={stock}&from=2024-01-01&to=2024-12-31&token={FINNHUB_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return [item['headline'] for item in data[:5]]

def get_yahoo_news(stock):
    url = f'https://finance.yahoo.com/quote/{stock}/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    headlines = [item.text for item in soup.select('h3 a')][:5]
    return headlines

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # [-1, 1]

def main():
    results = []
    for stock in STOCKS:
        titles = []

        try:
            titles += get_newsapi_news(stock)
        except Exception as e:
            print(f"NewsAPI error for {stock}: {e}")

        try:
            titles += get_finnhub_news(stock)
        except Exception as e:
            print(f"Finnhub error for {stock}: {e}")

        try:
            titles += get_yahoo_news(stock)
        except Exception as e:
            print(f"Yahoo scrape error for {stock}: {e}")

        if not titles:
            print(f"No news for {stock}")
            continue

        print(f"{stock}: {len(titles)} titres récupérés")

        sentiments = [analyze_sentiment(title) for title in titles]
        if len(sentiments) == 0:
            print(f"No sentiments computed for {stock}")
            continue

        avg_sentiment = sum(sentiments) / len(sentiments)
        probability = max(0, min(1, (avg_sentiment + 1) / 2)) * 100  # [0,100]
        results.append({'stock': stock, 'probability': probability})
