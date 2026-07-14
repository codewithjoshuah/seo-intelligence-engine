from crawler import crawl

from keywords.extractor import extract


domain = input("Website: ")

pages = crawl(domain)

keywords = extract(pages)

print()

print(f"Pages: {len(pages)}")

print(f"Keywords: {len(keywords)}")

print()

print(f"{'Keyword':30}{'Freq':>8}{'Pages':>8}")

print("-" * 50)

for keyword in keywords[:50]:

    print(
        f"{keyword.phrase:30}"
        f"{keyword.frequency:>8}"
        f"{keyword.pages:>8}"
    )