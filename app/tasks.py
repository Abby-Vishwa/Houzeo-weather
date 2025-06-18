import os
from celery import Celery
from .news_api import fetch_top_headlines, save_articles

celery_app = Celery(
    "worker",
    broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0"),
)

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # runs every minute
    sender.add_periodic_task(60.0, fetch_and_store.s())

@celery_app.task
def fetch_and_store():
    data = fetch_top_headlines()
    save_articles(data)
