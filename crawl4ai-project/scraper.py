import asyncio
import os
from slugify import slugify
from crawl4ai import AsyncWebCrawler
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

async def save_markdown(result):
    """Save scraped content to markdown file with enhanced logging"""
    try:
        if result.success and len(result.markdown) > 500:  # Minimum content check
            # Clean up the markdown content
            lines = result.markdown.split("\n")
            clean_lines = []
            skip_next = False
            in_code_block = False
            in_menu_section = False
            
            for line in lines:
                # Handle code blocks
                if line.strip().startswith("```"):
                    in_code_block = not in_code_block
                    clean_lines.append(line)
                    continue
                
                if in_code_block:
                    clean_lines.append(line)
                    continue
                
                # Detect menu sections
                if any(phrase.lower() in line.lower() for phrase in [
                    "navigation", "menu", "sidebar", "footer", "header",
                    "categories", "sections", "quick links", "related links"
                ]):
                    in_menu_section = True
                    continue
                
                # Skip content within menu sections
                if in_menu_section:
                    if not line.strip():  # End of menu section
                        in_menu_section = False
                    continue
                
                # Skip empty lines and markdown links
                if not line.strip() or line.strip().startswith("["):
                    continue
                
                # Skip lines after section headers
                if skip_next and not line.strip():
                    skip_next = False
                    continue
                
                clean_lines.append(line)
            
            clean_markdown = "\n".join(clean_lines)

            filename = slugify(result.url) + ".md"
            filepath = os.path.join("saved-docs", filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# URL: {result.url}\n\n")
                f.write(f"**Scraped At:** {datetime.now()}\n\n")
                f.write(clean_markdown)
            ScraperLogger.log_success(result.url)
            print(f"✅ Saved: {filepath}")
        else:
            error_msg = result.error or "Insufficient content"
            ScraperLogger.log_failure(result.url, error_msg)
            print(f"❌ Failed: {result.url} - {error_msg}")
    except Exception as e:
        ScraperLogger.log_failure(result.url, str(e))
        print(f"🔥 Error saving {result.url}: {str(e)}")

async def main():
    """Main scraping workflow with performance tracking"""
    start_time = datetime.now()
    
    # Load URLs from file
    with open("urls.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    
    # Configure crawler without proxy support
    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun_many(
            urls=urls,
            max_concurrent=4,
            delay_seconds=2.0,
            retry_attempts=3,
            session_group="main",
            follow_links=True,  # Enable subpage crawling
            max_depth=2,       # How many levels deep to crawl
            same_domain=True,  # Only follow links within same domain
            link_selector="nav a, .menu a, footer a",  # CSS selectors for menu links
            exclude_patterns=[  # Patterns to exclude
                ".*\\.pdf$",
                ".*\\.jpg$",
                ".*/tag/.*"
            ]
        )
        
        # Save results concurrently
        await asyncio.gather(*[save_markdown(r) for r in results])
    
    # Print performance summary
    duration = datetime.now() - start_time
    print(f"\n🏁 Scraping completed in {duration.total_seconds():.2f} seconds")
    success_count = len([r for r in results if r.success])
    print(f"📊 Success rate: {success_count}/{len(urls)} ({success_count/len(urls):.0%})")

if __name__ == "__main__":
    asyncio.run(main())
