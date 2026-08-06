import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://lei.lums.edu.pk/"


def discover_links():
    response = requests.get(BASE_URL)

    soup = BeautifulSoup(response.text, "lxml")

    links = set()

    for a in soup.find_all("a", href=True):

        href = a["href"]

        full_url = urljoin(BASE_URL, href)

        full_url = full_url.split("#")[0]

        if full_url.startswith(BASE_URL):
            links.add(full_url)

    return sorted(links)


if __name__ == "__main__":

    urls = discover_links()

    for url in urls:
        print(url)