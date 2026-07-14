from crawler.fetcher import fetch
from crawler.parser import parse

url = input("URL: ")

html = fetch(url)

page = parse(url, html)

print()

print("Title:")
print(page.title)

print()

print("Description:")
print(page.description)

print()

print("Language:")
print(page.language)

print()

print("Canonical:")
print(page.canonical)

print()

print("H1:")
print(page.h1)

print()

print("H2:")
print(page.h2)

print()

print("Word Count:")
print(page.word_count)