from flask import Flask, request
from config import WEBHOOK_SECRET
from db import init_db
import os

app = Flask(__name__)

# Inline webhook handler
@app.route(f"/webhook/{WEBHOOK_SECRET}", methods=["POST"])
def webhook():
    data = request.json
    print("Received webhook data:", data)
    # TODO: Add your processing logic here
    return "", 200

@app.route("/")
def home():
    return "RepeatBot is live!"

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
