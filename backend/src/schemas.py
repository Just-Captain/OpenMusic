from pydantic import BaseModel

class UserSchemaCreate(BaseModel):
    username:str
    password:str
    telegram_id: int| None = None


class QueryMusicSchema(BaseModel):
    telegram_id: int | None = None
    username: str | None = None
    query: str