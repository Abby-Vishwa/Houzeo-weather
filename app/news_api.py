import os
import requests
from datetime import datetime
from .database import SessionLocal
from .models import NewsArticle

NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "")
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"


def fetch_top_headlines(country="us"):
    params = {"apiKey": NEWS_API_KEY, "country": country}
    response = requests.get(NEWS_API_URL, params=params)
    response.raise_for_status()
    return response.json()


def save_articles(data):
    session = SessionLocal()
    try:
        for article in data.get("articles", []):
            news = NewsArticle(
                title=article.get("title"),
                description=article.get("description"),
                url=article.get("url"),
                published_at=datetime.fromisoformat(article.get("publishedAt", "").replace("Z", "+00:00")) if article.get("publishedAt") else None,
            )
            session.add(news)
        session.commit()
    finally:
        session.close()
