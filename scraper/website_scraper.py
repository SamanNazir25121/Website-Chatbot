import requests
from bs4 import BeautifulSoup
from scraper.extractor import extract_structured_text


def scrape_page(url):

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed: {url}")
        return None

    soup = BeautifulSoup(response.text, "lxml")

    # Remove unwanted elements
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = extract_structured_text(
    soup
)
    return text