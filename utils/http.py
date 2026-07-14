import requests

from config import HEADERS, TIMEOUT, VERIFY_SSL


def get(url: str):

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=TIMEOUT,
            verify=VERIFY_SSL,
        )

        response.raise_for_status()

        return response

    except requests.RequestException:
        return None