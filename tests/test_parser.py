from crawler.fetcher import fetch
from crawler.parser import parse

url = input("URL: ")

html = fetch(url)

page = parse(url, html)

print()

print("Title:")
print(page.title)

print()

print("Text Preview:")
print(page.text[:1500])