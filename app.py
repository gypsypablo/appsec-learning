# test

import os
import sqlite3
import requests

# 1. ИСПРАВЛЕНИЕ СЕКРЕТА: Убираем токен из кода
# Вместо зашитой строки мы берем токен из переменных окружения (Environment Variables)
# На сервере (или в GitHub Actions) мы положим его в секреты, и код подтянет его на лету
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # 2. ИСПРАВЛЕНИЕ SQLi: Используем параметризованный запрос (Parameterized Query)
    # Вместо f-строки мы ставим знак вопроса '?'. 
    # Теперь библиотека sqlite3 сама очистит и безопасно вставит переменную username,
    # полностью исключая возможность внедрения вредоносного SQL-кода.
    query = "SELECT * FROM users WHERE username = ?"
    
    cursor.execute(query, (username,))
    return cursor.fetchall()

def send_notification(message):
    if SLACK_WEBHOOK_URL:
        requests.post(SLACK_WEBHOOK_URL, json={"text": message})