import os
BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
TEST_USER = os.getenv("TEST_USER", "")
TEST_PASSWORD = os.getenv("TEST_PASSWORD", "")
DEFAULT_TIMEOUT = os.getenv("DEFAULT_TIMEOUT", "15s")
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))
