import sys

from crawler import crawl
from keywords.extractor import extract

if len(sys.argv) < 2:
    print("Usage: python main.py <website>")
    sys.exit(1)

domain = sys.argv[1]

pages = crawl(domain)

keywords = extract(pages)
with open("output/report.md", "w", encoding="utf-8") as f:

    f.write("# SEO Intelligence Report\n\n")

    f.write(f"Website: {domain}\n\n")

    f.write(f"Pages Crawled: {len(pages)}\n\n")

    f.write(f"Keywords Found: {len(keywords)}\n\n")

    f.write("## Top Keywords\n\n")

    for keyword in keywords[:20]:

        f.write(
            f"- {keyword.phrase} ({keyword.frequency})\n"
        )

print(f"\nFound {len(keywords)} keywords")