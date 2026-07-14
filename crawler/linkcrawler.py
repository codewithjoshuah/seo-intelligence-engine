from collections import deque
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from config import MAX_PAGES
from crawler.fetcher import fetch


def urls(start_url: str) -> list[str]:

    visited = set()

    queue = deque([start_url])

    discovered = []

    domain = urlparse(start_url).netloc

    while queue:

        if MAX_PAGES and len(visited) >= MAX_PAGES:
            break

        url = queue.popleft()

        if url in visited:
            continue

        visited.add(url)

        html = fetch(url)

        if not html:
            continue

        discovered.append(url)

        soup = BeautifulSoup(html, "html.parser")

        for a in soup.find_all("a", href=True):

            link = urljoin(url, a["href"])

            parsed = urlparse(link)

            if parsed.netloc != domain:
                continue

            clean = (
                parsed.scheme
                + "://"
                + parsed.netloc
                + parsed.path
            )

            if clean not in visited:
                queue.append(clean)

    return sorted(discovered)