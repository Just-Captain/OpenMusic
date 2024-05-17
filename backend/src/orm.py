import sqlite3

class UserCrud:
    __instance = None

    def __new__ (cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db) -> None:
        self.db = db

    def add(self, username: str, password: str, telegram_id=None):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        if telegram_id:
            cursor.execute('''
            INSERT INTO users (username, password, telegram_id) VALUES (?, ?, ?)
            ''',(username, password, telegram_id))
            
        else:
            cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?)
            ''', (username, password))
        connect.commit()
        connect.close()

    def get_user_web(self, username:str):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        sql = f'SELECT * FROM users WHERE username = {username}'
        cursor.execute(sql)
        user = cursor.fetchone()
        connect.close()
        return user

    def get_user_tg(self, telegram_id:int):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        sql = f'SELECT * FROM users WHERE telegram_id = {telegram_id}'
        cursor.execute(sql)
        user = cursor.fetchone()
        print(user, 'get_user_tg')
        connect.close()
        return user

    