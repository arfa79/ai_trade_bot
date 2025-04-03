import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_telegram_alert(message):
    """Send alerts via Telegram bot."""
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    requests.post(url, json=payload)

# Example: send_telegram_alert("BTC buy signal at $42,000")