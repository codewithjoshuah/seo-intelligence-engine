from pathlib import Path
import urllib3

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

PROJECT_NAME = "SEO Intelligence Engine"

VERSION = "1.0.0"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(X11; Linux x86_64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}

TIMEOUT = 20

VERIFY_SSL = False

MAX_THREADS = 10

MAX_PAGES = 100

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)