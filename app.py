# Testing here again and again and again and again and again and again

import sqlite3

# Тестовый приватный ключ для проверки сканера секретов
DUMMY_PRIVATE_KEY = """
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtcn
NhAAAAAwEAAQAAAYEAm16R+V7vJ2yG8mK6ZlP0C9f+Y3XFpZ1234567890abcdefghij
-----END OPENSSH PRIVATE KEY-----
"""

# Настоящий паттерн Slack Webhook. TruffleHog триггерится на него моментально! (testing)
SLACK_WEBHOOK = "https://hooks.slack.com/services/T01234567/B01234567/Tk9UX0FfUkVBTF9UT0tFTl9KVVNUX1RFU1RJTkc="



db_password = "MySuperSecretPassword123"



def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # 2. УЯЗВИМОСТЬ: SQL Injection (SQL-инъекция)
    # Переменная username вставляется напрямую в запрос. Semgrep должен это поймать!
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    cursor.execute(query)
    return cursor.fetchall()