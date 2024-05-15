import sqlite3

def create_table_database():
    connect = sqlite3.connect('./database.sqlite3')
    cursor = connect.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username VARCHAR(30) NOT NULL UNIQUE,
                   password VARCHAR(255) NOT NULL,
                   telegram_id INTEGER
    )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS musics (
                   music_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   query_user TEXT NOT NULL,
                   url_music TEXT,
                   FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
    )
''')
    connect.commit()
    connect.close()
    print('Table create')
