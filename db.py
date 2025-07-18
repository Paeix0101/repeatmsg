import mysql.connector
from config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id BIGINT PRIMARY KEY,
        first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS groups_channels (
        id BIGINT PRIMARY KEY,
        type ENUM('group', 'channel') NOT NULL,
        first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS repeat_messages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        chat_id BIGINT,
        message_id BIGINT,
        repeat_slot ENUM('repeat1', 'repeat2'),
        file_id TEXT,
        text TEXT,
        next_run TIMESTAMP,
        interval_minutes INT,
        last_sent_msg_id BIGINT,
        is_active BOOLEAN DEFAULT TRUE
    )""")

    conn.commit()
    cursor.close()
    conn.close()
