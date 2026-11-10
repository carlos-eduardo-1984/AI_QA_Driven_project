import os
from config.environments.common import *
ENVIRONMENT = "integration"
WEB_BASE_URL = os.getenv("INTEGRATION_WEB_BASE_URL", "https://integration.example.test")
API_BASE_URL = os.getenv("INTEGRATION_API_BASE_URL", "https://api.integration.example.test")
