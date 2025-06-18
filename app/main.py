from fastapi import FastAPI
from .database import engine, Base
from .models import NewsArticle

Base.metadata.create_all(bind=engine)

app = FastAPI(title="News Fetcher")

@app.get("/articles")
def list_articles():
    from .database import SessionLocal
    session = SessionLocal()
    try:
        articles = session.query(NewsArticle).order_by(NewsArticle.published_at.desc()).all()
        return [
            {
                "id": a.id,
                "title": a.title,
                "description": a.description,
                "url": a.url,
                "published_at": a.published_at,
            }
            for a in articles
        ]
    finally:
        session.close()
