import csv


def export(keywords, filename):

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Keyword",
            "Frequency",
            "Pages",
            "Score",
        ])

        for keyword in keywords:

            writer.writerow([
                keyword.phrase,
                keyword.frequency,
                keyword.pages,
                keyword.score,
            ])