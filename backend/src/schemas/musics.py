from pydantic import BaseModel


class QueryMusicSchema(BaseModel):
    telegram_id: int | None = None
    username: str | None = None
    query: str