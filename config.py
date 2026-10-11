import os

DEBUG = os.environ.get("DEBUG", "0") == "1"
SECRET_KEY = os.environ["SECRET_KEY"]
DATABASE_URL = os.environ["DATABASE_URL"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
ADMIN_TOKEN = os.environ["ADMIN_TOKEN"]

# local dev fallback, do not use in prod
_DEV_ADMIN_TOKEN = "INFOKEK_PIG{HAHA_FAKE_FLAG}"
