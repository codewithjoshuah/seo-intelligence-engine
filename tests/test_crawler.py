from crawler import crawl

domain = input("Website: ")

pages = crawl(domain)

print()

print(f"Crawled {len(pages)} pages\n")

for page in pages[:5]:

    print("=" * 80)

    print(page.title)

    print(page.url)

    print(page.text[:300])

    print()