import os
import sqlite3
import requests

# Теперь секрет подтягивается из окружения операционной системы или контейнера.
# В коде больше нет текстовых паттернов, на которые мог бы среагировать TruffleHog.
SLACK_LOGS_WEBHOOK = os.environ.get("SLACK_LOGS_WEBHOOK_URL")

def send_slack_alert(message):
    """Функция отправки системных алертов в Slack логгер"""
    if not SLACK_LOGS_WEBHOOK:
        # Если переменная не задана (например, при локальной разработке), 
        # код не упадет, а просто пропустит отправку
        return False
        
    payload = {"text": f"🚨 System Alert: {message}"}
    try:
        response = requests.post(SLACK_LOGS_WEBHOOK, json=payload, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def get_user_data(username):
    # Безопасный параметризованный запрос (Semgrep по-прежнему доволен)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    user = cursor.fetchall()
    
    # Отправка алерта работает через безопасную переменную
    send_slack_alert(f"User data requested for username: {username}")
    
    return user