import os
import requests
from flask import Flask, request
from config import WEBHOOK_SECRET, BOT_TOKEN
from db import init_db

app = Flask(__name__)

# Webhook route
@app.route(f"/webhook/{WEBHOOK_SECRET}", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook data:", data)
    # TODO: Handle updates (currently basic)
    return "", 200

# Health check route
@app.route("/")
def home():
    return "RepeatBot is live!"

def set_webhook():
    render_url = "https://repeatmsg.onrender.com"  # ✅ Your real Render domain
    full_webhook_url = f"{render_url}/webhook/{WEBHOOK_SECRET}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    response = requests.get(url, params={"url": full_webhook_url})
    print("Set webhook response:", response.json())

if __name__ == "__main__":
    init_db()
    set_webhook()  # ✅ Set webhook once on start
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

