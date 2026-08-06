from scraper.crawler import discover_links
from scraper.website_scraper import scrape_page
from scraper.storage import save_document
from scraper.cleaner import clean_text
from scraper.metadata import create_metadata, save_metadata

documents = []

urls = discover_links()
print(f"\nFound {len(urls)} pages\n")

for url in urls:
    print(f"Scraping {url}")

    text = scrape_page(url)

    if text:
        cleaned_text = clean_text(text)

        filename = url.split("/")[-1] or "index.html"
        filename = filename.replace(".html", ".txt")

        save_document(filename, cleaned_text)

        documents.append(
            create_metadata(
                filename,
                cleaned_text,
                url
            )
        )

save_metadata(documents)

print("\nDone!")