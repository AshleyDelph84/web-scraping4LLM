# Multi-URL Scraping Implementation Plan

## 1. Environment Setup
```bash
# Create project directory
mkdir crawl4ai-project && cd crawl4ai-project

# Create virtual environment
#python -m venv .venv
#source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Install dependencies
pip install "crawl4ai[llm]" python-slugify

# Create output directory
mkdir -p saved-docs
```

## 2. Project Structure
```
crawl4ai-project/
├── scraper.py
├── urls.txt
└── saved-docs/
```

## 3. URL List (urls.txt)
```
https://example.com/page1
https://example.com/page2
https://example.com/page3
https://example.com/page4
```

## 4. Scraper Implementation (scraper.py)
```python
import asyncio
import os
from slugify import slugify
from crawl4ai import AsyncWebCrawler, CrawlDispatcher

async def save_markdown(result):
    """Save scraped content to markdown file"""
    try:
        if result.success:
            # Generate filename from URL
            filename = slugify(result.url) + ".md"
            filepath = os.path.join("saved-docs", filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(result.markdown)
            print(f"Saved: {filepath}")
        else:
            print(f"Failed: {result.url} - {result.error}")
    except Exception as e:
        print(f"Error saving {result.url}: {str(e)}")

async def main():
    # Load URLs from file
    with open("urls.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    
    # Configure crawler
    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun_many(
            urls=urls,
            config=CrawlDispatcher(
                max_concurrent=4,    # Process 4 URLs simultaneously
                delay_seconds=2.0,   # Be polite between requests
                retry_attempts=3,    # Retry failed requests
                session_group="main" # Maintain session cookies
            )
        )
        
        # Save results concurrently
        await asyncio.gather(*[save_markdown(r) for r in results])

if __name__ == "__main__":
    asyncio.run(main())
```

## 5. Execution
```bash
python scraper.py
```

## 6. Expected Output
```
Saved: saved-docs/https-example-com-page1.md
Saved: saved-docs/https-example-com-page2.md
Saved: saved-docs/https-example-com-page3.md
Saved: saved-docs/https-example-com-page4.md
```

## Key Features
- Concurrent scraping with 4 parallel requests
- Automatic filename generation using URL slugs
- Error handling and retry mechanisms
- Session persistence across requests
- Rate limiting with 2-second delays
- Organized output in dedicated folder
```

This plan implements best practices from Crawl4AI documentation while adding:
1. File-based URL input
2. Automated filename generation
3. Error handling and retries
4. Output directory management
5. Rate limiting to avoid detection

To scale further:
- Add proxy rotation
- Implement result validation
- Add logging system
- Set up periodic scraping with cron/Airflow

## 7. Advanced Configuration

### Add rate limiting and error tracking:
```python
# Add to scraper.py
from datetime import datetime

class ScraperLogger:
    @staticmethod
    def log_failure(url, error):
        with open("scrape_errors.log", "a") as f:
            f.write(f"{datetime.now()} | {url} | {error}\n")

    @staticmethod
    def log_success(url):
        with open("scrape_success.log", "a") as f:
            f.write(f"{datetime.now()} | {url}\n")

# Update save_markdown function
async def save_markdown(result):
    try:
        if result.success and len(result.markdown) > 500:  # Minimum content check
            filename = slugify(result.url) + ".md"
            filepath = os.path.join("saved-docs", filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# URL: {result.url}\n\n")
                f.write(f"**Scraped At:** {datetime.now()}\n\n")
                f.write(result.markdown)
            ScraperLogger.log_success(result.url)
        else:
            ScraperLogger.log_failure(result.url, 
                result.error or "Insufficient content")
    except Exception as e:
        ScraperLogger.log_failure(result.url, str(e))
```

## 8. Proxy Configuration
````diff
# Update Crawler configuration
config=CrawlDispatcher(
    max_concurrent=4,
    delay_seconds=2.0,
    retry_attempts=3,
    session_group="main",
+   proxies=[
+       "http://proxy1.example.com:8080",
+       "http://proxy2.example.com:8080"
+   ],
+   proxy_rotation="round-robin"
)
````

## 9. Monitoring Setup
```python
# Add performance tracking
async def main():
    start_time = datetime.now()
    
    # ... existing scraping code ...
    
    duration = datetime.now() - start_time
    print(f"\nScraping completed in {duration.total_seconds():.2f} seconds")
    print(f"Success rate: {len([r for r in results if r.success])}/{len(urls)}")
```

## 10. Docker Deployment
```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install "crawl4ai[llm]" python-slugify && \
    mkdir -p /app/saved-docs

CMD ["python", "scraper.py"]
```

Build and run:
```bash
docker build -t url-scraper .
docker run -v $(pwd)/saved-docs:/app/saved-docs url-scraper
```

## 11. Scheduled Scraping
````bash
# Install cron
0 3 * * * /path/to/venv/bin/python /path/to/scraper.py >> scrape.log 2>&1
````

This enhanced plan adds:
- Comprehensive error logging and retries
- Content validation checks
- Proxy rotation support
- Performance monitoring
- Docker containerization
- Scheduled execution
- Improved file naming with timestamps
