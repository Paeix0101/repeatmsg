from flask import request
from config import BOT_USERNAME
from db import get_connection

def webhook():
    data = request.get_json()
    print("📩 Received Telegram update:", data)

    if not data or "message" not in data:
        return "ok", 200

    msg = data["message"]
    chat_id = msg["chat"]["id"]
    chat_type = msg["chat"]["type"]
    user_id = msg["from"]["id"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT IGNORE INTO users (id) VALUES (%s)", (user_id,))
    if chat_type in ["group", "supergroup", "channel"]:
        cursor.execute("INSERT IGNORE INTO groups_channels (id, type) VALUES (%s, %s)", (chat_id, chat_type))

    conn.commit()
    cursor.close()
    conn.close()

    return "ok", 200