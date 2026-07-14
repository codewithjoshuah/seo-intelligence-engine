from utils.http import get


def fetch(url: str) -> str:
    """
    Download a webpage and return its HTML.
    """

    try:

        response = get(url)

        response.raise_for_status()

        content_type = response.headers.get(
            "Content-Type",
            ""
        ).lower()

        if "text/html" not in content_type:
            return ""

        return response.text

    except Exception:

        return ""