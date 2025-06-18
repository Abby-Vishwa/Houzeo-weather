from sqlalchemy import Column, Integer, String, Text, DateTime
from .database import Base

class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(512))
    description = Column(Text)
    url = Column(String(1024))
    published_at = Column(DateTime)
