import sqlite3

from models.users import UserModel


class UserCrud:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db) -> None:
        self.db = db

    def create_user(
            self,
            username: str,
            password: str,
            telegram_id=None
    ):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        if telegram_id:
            cursor.execute('''
            INSERT INTO users (username, password, telegram_id) VALUES (?, ?, ?)
            ''', (username, password, telegram_id))

        else:
            cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?)
            ''', (username, password))
        connect.commit()
        connect.close()



    def all(self):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        rows = cursor.fetchall()
        connect.close()
        users = [UserModel(*user).to_dict() for user in rows]
        return {"users": users}

    def get(
            self,
            user_id: int | None = None,
            username: str | None = None,
            telegram_id: int | None = None
    ) -> UserModel:
        if user_id:
            connect = sqlite3.connect(self.db)
            cursor = connect.cursor()
            sql = 'SELECT * FROM users WHERE id = ?'
            cursor.execute(sql, (user_id,))
            row = cursor.fetchone()
            connect.close()
            if row is not None:
                return UserModel(*row)
        elif username:
            connect = sqlite3.connect(self.db)
            cursor = connect.cursor()
            sql = 'SELECT * FROM users WHERE username = ?'
            cursor.execute(sql, (username,))
            row = cursor.fetchone()
            connect.close()
            if row is not None:
                return UserModel(*row)
        elif telegram_id:
            connect = sqlite3.connect(self.db)
            cursor = connect.cursor()
            sql = 'SELECT * FROM users WHERE telegram_id = ?'
            cursor.execute(sql, (telegram_id,))
            row = cursor.fetchone()
            connect.close()
            if row is not None:
                return UserModel(*row)
        else:
            return ValueError('Please provide')



