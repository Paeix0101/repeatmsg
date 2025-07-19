import requests
from config import BOT_TOKEN, WEBHOOK_SECRET

render_url = "https://repeatmsg.onrender.com"  # 🔁 Replace with your Render domain
webhook_url = f"{render_url}/webhook/{WEBHOOK_SECRET}"

response = requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook",
    params={"url": webhook_url}
)

print(response.status_code, response.text)