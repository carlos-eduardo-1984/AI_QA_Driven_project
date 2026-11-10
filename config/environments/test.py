import os
from config.environments.common import *
ENVIRONMENT = "test"
WEB_BASE_URL = os.getenv("TEST_WEB_BASE_URL", "https://test.example.test")
API_BASE_URL = os.getenv("TEST_API_BASE_URL", "https://api.test.example.test")
