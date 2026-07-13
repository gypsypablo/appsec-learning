import sqlite3

# 1. УЯЗВИМОСТЬ: Hardcoded Secret (Зашитый секрет)
# TruffleHog должен это поймать!
AWS_SECRET_KEY = "AKIAIMXFFAOXEXAMPLE_SECRET_KEY_12345"

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # 2. УЯЗВИМОСТЬ: SQL Injection (SQL-инъекция)
    # Переменная username вставляется напрямую в запрос. Semgrep должен это поймать!
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    cursor.execute(query)
    return cursor.fetchall()