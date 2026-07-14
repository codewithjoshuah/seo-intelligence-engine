import logging
from utils.logger import log

log.info("Reading sitemap...")
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)

log = logging.getLogger("seo")

