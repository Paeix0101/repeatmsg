import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
BOT_USERNAME = os.getenv("BOT_USERNAME")

DB_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'database': os.getenv("DB_NAME"),
    'port': int(os.getenv("DB_PORT", 3306))  # This line is important!
}

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
OWNER_ID = 8141547148  # Your Telegram ID

