import os
import requests
from flask import Flask
from config import WEBHOOK_SECRET, BOT_TOKEN
from db import init_db
from webhook_handler import webhook as handle_webhook

app = Flask(__name__)

@app.route(f"/webhook/{WEBHOOK_SECRET}", methods=["POST"])
def webhook():
    print("✅ Webhook hit!")
    return handle_webhook()

@app.route("/")
def home():
    return "✅ RepeatBot is live!"

def set_webhook():
    render_url = "https://repeatmsg.onrender.com"  # ✅ Use your real domain
    full_webhook_url = f"{render_url}/webhook/{WEBHOOK_SECRET}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    response = requests.get(url, params={"url": full_webhook_url})
    print("Set webhook response:", response.json())

if __name__ == "__main__":
    print("WEBHOOK_SECRET:", WEBHOOK_SECRET)  # Debug check
    init_db()
    set_webhook()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


