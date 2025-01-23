# Crawl4AI Documentation Summary

## Overview
🚀 **Crawl4AI** is an open-source, LLM-friendly web crawler & scraper designed for AI workflows. Key features:
- Generates clean Markdown for RAG pipelines
- Structured extraction (CSS/XPath/LLM-based)
- Advanced browser control with proxies & stealth modes
- High-performance parallel crawling
- MIT Licensed (free for commercial use)

## Key Capabilities
- **Web Crawling**: Async-first architecture with configurable depth
- **Content Processing**:
  - Automatic HTML-to-Markdown conversion
  - Content filtering and selection
  - Media/link extraction
- **Extraction Strategies**:
  - CSS/XPath selectors
  - LLM-based extraction (supports OpenAI & OSS models)
  - Clustering/chunking for large documents

## Installation
```bash
# Basic installation
pip install crawl4ai

# With LLM dependencies
pip install "crawl4ai[llm]" 

# Docker option available
docker pull unclecode/crawl4ai
```

## Quick Start
```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com",
            config={"include_images": True}
        )
        print(result.markdown)

asyncio.run(main())
```

## Core Components
1. **BrowserConfig** - Control headless browser behavior:
   - User agents, viewport sizes
   - JavaScript execution
   - Screenshot capture

2. **CrawlerRunConfig** - Crawling parameters:
   - Max pages/depth
   - Delay between requests
   - Cache policies

3. **Extraction Strategies**:
   - `CSSStrategy`: CSS selector-based
   - `LLMStrategy`: GPT-4/Claude/Mistral
   - `ClusterStrategy`: Content clustering

## Advanced Features
- Dynamic content handling (infinite scroll/SPAs)
- Proxy rotation & CAPTCHA avoidance
- Custom hooks for authentication
- Session management
- SSL certificate handling
- File downloading
- **Multi-URL Crawling**:
  - Batch processing of URLs
  - Configurable concurrency limits
  - Session persistence across requests

## Multi-URL Crawling Setup
```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlDispatcher

async def main():
    urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
    ]
    
    async with AsyncWebCrawler() as crawler:
        # Parallel crawling with browser instance reuse
        results = await crawler.arun_many(
            urls=urls,
            config=CrawlDispatcher(
                max_concurrent=3,  # Simultaneous tabs
                delay_seconds=1.5  # Between requests
            )
        )
        
        for result in results:
            print(f"URL: {result.url}")
            print(f"Content length: {len(result.markdown)}")

asyncio.run(main())
```

Key parameters:
- `max_concurrent`: Number of parallel browser tabs (default: 3)
- `delay_seconds`: Delay between requests to avoid detection
- `session_group`: Group related requests for cookie sharing
- `retry_attempts`: Number of retries for failed requests

## Integration
```python
# PraisonAI Integration Example
from praisonai import PraisonAI
from crawl4ai import CSSStrategy

praison = PraisonAI()
praison.add_tool(
    "web_scraper",
    AsyncWebCrawler(),
    strategy=CSSStrategy(selectors=["main-content"])
)
```

## Resources
- [Official Documentation](https://docs.crawl4ai.com)
- [GitHub Repository](https://github.com/unclecode/crawl4ai)
- [Changelog](https://docs.crawl4ai.com/blog/changelog)
