class UserModel:
    def __init__(self, user_id: int, username: str, password: str, telegram_id: int | None = None) -> None:
        self.user_id = user_id
        self.username = username
        self.password = password
        self.telegram_id = telegram_id

    def to_dict(self) -> dict:
        return dict(user_id=self.user_id, username=self.username, password=self.password, telegram_id=self.telegram_id)

    def to_json(self) -> dict:
        return dict(user_id=self.user_id, username=self.username, telegram_id=self.telegram_id)

