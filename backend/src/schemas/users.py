from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    username: str
    password: str
    telegram_id: int | None = None


class UserLoginSchema(BaseModel):
    username: str
    password: str

class UserRegisterSchema(BaseModel):
    username: str
    password: str
    telegram_id: int | None = None
