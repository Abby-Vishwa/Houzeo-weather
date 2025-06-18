# News API Fetcher

This project uses FastAPI and Celery to periodically fetch news articles from the [News API](https://newsapi.org/) and store them in a MySQL database.

## Requirements

- Python 3.11+
- MySQL database
- Redis (for Celery broker and backend)

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Create the environment variables `NEWS_API_KEY` and `DATABASE_URL` pointing to your News API key and MySQL database respectively. Example:

```bash
export NEWS_API_KEY=your_api_key
export DATABASE_URL=mysql+pymysql://user:password@localhost/newsdb
```

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

## Running the Celery worker

Start a Redis server then run:

```bash
celery -A app.tasks worker -B --loglevel=info
```

The `-B` flag enables Celery Beat which schedules the periodic task every minute.
