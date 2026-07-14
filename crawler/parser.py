from bs4 import BeautifulSoup

from models.page import Page

REMOVE = [
    "script",
    "style",
    "noscript",
    "svg",
    "iframe",
    "header",
    "footer",
    "nav",
]


def parse(url: str, html: str):

    if not html:
        return None

    soup = BeautifulSoup(html, "lxml")

    for tag in soup(REMOVE):
        tag.decompose()

    page = Page(url=url)

    if soup.title:
        page.title = soup.title.get_text(strip=True)

    meta = soup.find("meta", attrs={"name": "description"})
    if meta:
        page.description = meta.get("content", "").strip()

    canonical = soup.find("link", rel="canonical")
    if canonical:
        page.canonical = canonical.get("href", "").strip()

    html_tag = soup.find("html")
    if html_tag:
        page.language = html_tag.get("lang", "")

    page.h1 = [
        h.get_text(" ", strip=True)
        for h in soup.find_all("h1")
    ]

    page.h2 = [
        h.get_text(" ", strip=True)
        for h in soup.find_all("h2")
    ]

    page.text = soup.get_text(" ", strip=True)

    page.word_count = len(page.text.split())

    return page