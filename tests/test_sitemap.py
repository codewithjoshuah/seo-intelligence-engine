from crawler.sitemap import discover, urls

domain = input("Website: ").strip()

print("\nDiscovering sitemap...")
sitemap = discover(domain)

print("Sitemap:", sitemap)

print("\nReading sitemap...")
pages = urls(sitemap)

print(f"\nFound {len(pages)} pages")

print("\nFirst 10 pages:")

for page in pages[:10]:
    print(page)