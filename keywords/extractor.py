from collections import Counter

from keywords.cleaner import clean
from keywords.stopwords import STOPWORDS
from models.keyword import Keyword


def extract(pages):

    frequency = Counter()

    page_frequency = Counter()

    for page in pages:

        words = []

        text = clean(page.text)

        for word in text.split():

            if len(word) < 3:
                continue

            if word in STOPWORDS:
                continue

            words.append(word)

        frequency.update(words)

        page_frequency.update(set(words))

    keywords = []

    for word in frequency:

        keywords.append(

            Keyword(
                phrase=word,
                frequency=frequency[word],
                pages=page_frequency[word],
            )

        )

    keywords.sort(
        key=lambda x: x.frequency,
        reverse=True,
    )

    return keywords