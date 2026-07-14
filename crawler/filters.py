from urllib.parse import urlparse


SKIP_PATHS = [
    "/wp-admin",
    "/login",
    "/logout",
    "/cart",
    "/checkout",
    "/account",
    "/privacy",
    "/cookie",
    "/cookies",
    "/terms",
]


SKIP_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    ".webp",
    ".ico",
    ".pdf",
    ".zip",
    ".css",
    ".js",
    ".xml",
}


def clean(urls: list[str]) -> list[str]:
    """
    Remove duplicate, unwanted and non-HTML URLs.
    """

    cleaned = []

    for url in urls:

        path = urlparse(url).path.lower()

        # Skip unwanted folders
        if any(skip in path for skip in SKIP_PATHS):
            continue

        # Skip files
        if "." in path.split("/")[-1]:

            ext = "." + path.split(".")[-1]

            if ext in SKIP_EXTENSIONS:
                continue

        cleaned.append(url)

    return sorted(set(cleaned))