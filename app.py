import sqlite3
import requests

# Наш тестовый Slack Webhook для проверки TruffleHog
SLACK_LOGS_WEBHOOK = "https://hooks.slack.com/services/T01234567/B01234567/Tk9UX0FfUkVBTF9UT0tFTl9KVVNUX1RFU1RJTkc="

def send_slack_alert(message):
    """Функция отправки системных алертов в Slack логгер"""
    payload = {"text": f"🚨 System Alert: {message}"}
    try:
        response = requests.post(SLACK_LOGS_WEBHOOK, json=payload, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def get_user_data(username):
    # Безопасный параметризованный запрос (Semgrep будет доволен)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    user = cursor.fetchall()
    
    # Триггерим отправку алерта при запросе данных
    send_slack_alert(f"User data requested for username: {username}")
    
    return user