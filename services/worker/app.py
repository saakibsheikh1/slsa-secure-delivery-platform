
import logging
import os
import time
from datetime import datetime, timezone

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(message)s",
)

APP_NAME = "secure-delivery-worker"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
INTERVAL_SECONDS = int(os.getenv("INTERVAL_SECONDS", "30"))


def run_worker():
    logging.info(
        "Starting %s version %s",
        APP_NAME,
        APP_VERSION,
    )

    while True:
        logging.info(
            "Worker heartbeat: application=%s version=%s timestamp=%s",
            APP_NAME,
            APP_VERSION,
            datetime.now(timezone.utc).isoformat(),
        )
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    run_worker()
