from bs4 import BeautifulSoup


def extract_structured_text(soup):

    content = []


    # Extract headings
    for tag in soup.find_all(
        ["h1","h2","h3"]
    ):

        text = tag.get_text(
            strip=True
        )

        if text:
            content.append(
                text
            )


    # Extract paragraphs
    for p in soup.find_all("p"):

        text = p.get_text(
            strip=True
        )

        if text:
            content.append(
                text
            )


    # Extract list items
    for li in soup.find_all("li"):

        text = li.get_text(
            strip=True
        )

        if text:
            content.append(
                text
            )


    return "\n\n".join(content)
