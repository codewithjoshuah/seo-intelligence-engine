from crawler.fetcher import fetch

url = input("URL: ")

html = fetch(url)

print()

print("Downloaded:", len(html), "characters")

print()

print(html[:1000])