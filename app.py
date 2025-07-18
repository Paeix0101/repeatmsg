from flask import Flask
from config import WEBHOOK_SECRET
from db import init_db
from handlers.webhook_handler import webhook

app = Flask(__name__)
app.add_url_rule(f"/webhook/{WEBHOOK_SECRET}", view_func=webhook, methods=["POST"])

@app.route("/")
def home():
    return "RepeatBot is live!"

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))