from bs4 import BeautifulSoup

from utils.http import get


def discover(domain: str) -> str:
    """
    Discover the sitemap URL from robots.txt.
    Falls back to /sitemap.xml if none is found.
    """

    domain = domain.rstrip("/")

    response = get(f"{domain}/robots.txt")

    if response:

        for line in response.text.splitlines():

            if line.lower().startswith("sitemap:"):
                return line.split(":", 1)[1].strip()

    return f"{domain}/sitemap.xml"


def urls(sitemap_url: str) -> list[str]:
    """
    Read a sitemap (or sitemap index) and return all URLs.
    """

    response = get(sitemap_url)

    if response is None:
        print(f"Failed: {sitemap_url}")
        return []

    soup = BeautifulSoup(response.text, "xml")

    pages = []

    # Sitemap Index
    if soup.find("sitemapindex"):

        sitemaps = soup.find_all("sitemap")

        print(f"Found {len(sitemaps)} child sitemaps")

        for i, sitemap in enumerate(sitemaps, start=1):

            loc = sitemap.find("loc")

            if not loc:
                continue

            print(f"[{i}/{len(sitemaps)}] {loc.text}")

            pages.extend(urls(loc.text.strip()))

    # URL Sitemap
    else:

        for url in soup.find_all("url"):

            loc = url.find("loc")

            if loc:
                pages.append(loc.text.strip())

    return sorted(set(pages))