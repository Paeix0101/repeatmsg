from flask import Flask, request
from config import WEBHOOK_SECRET, API_URL
from db import init_db
import os
import requests

app = Flask(__name__)

# Webhook handler route (inline for now)
@app.route(f"/webhook/{WEBHOOK_SECRET}", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook data:", data)
    # TODO: Add your actual logic here
    return "", 200

@app.route("/")
def home():
    return "RepeatBot is live!"

def set_webhook():
    """Sets Telegram webhook on bot startup"""
    render_url = "https://your-render-url.onrender.com"  # 🔁 REPLACE with your actual Render domain
    webhook_url = f"{render_url}/webhook/{WEBHOOK_SECRET}"
    response = requests.post(f"{API_URL}/setWebhook", json={"url": webhook_url})

    if response.ok:
        print("✅ Webhook set successfully:", response.json())
    else:
        print("❌ Failed to set webhook:", response.text)

if __name__ == "__main__":
    init_db()
    set_webhook()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
