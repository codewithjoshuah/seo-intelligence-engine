from concurrent.futures import ThreadPoolExecutor, as_completed

from config import MAX_THREADS
from crawler.fetcher import fetch
from crawler.filters import clean
from crawler.linkcrawler import urls as link_urls
from crawler.parser import parse
from crawler.sitemap import discover, urls as sitemap_urls


def crawl(domain: str):

    print("Finding sitemap...")

    sitemap = discover(domain)

    page_urls = []

    if sitemap:

        print(f"Sitemap: {sitemap}")

        page_urls = clean(sitemap_urls(sitemap))

    if not page_urls:

        print("Using LinkCrawler...")

        page_urls = clean(link_urls(domain))

    print(f"{len(page_urls)} URLs discovered")

    pages = []

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:

        futures = {
            executor.submit(fetch, url): url
            for url in page_urls
        }

        for i, future in enumerate(as_completed(futures), start=1):

            url = futures[future]

            html = future.result()

            page = parse(url, html)

            if page:
                pages.append(page)

            if i % 10 == 0:
                print(f"Crawled {i}/{len(page_urls)}")

    return pages