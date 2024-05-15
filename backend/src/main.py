from fastapi import FastAPI, Request, status
import uvicorn
from database import create_table_database
from pydantic import BaseModel
from orm import UserCrud
app = FastAPI(
    title="OpenMusic API"
)

class UserSchemaCreate(BaseModel):
    username:str
    password:str
    telegram_id: int| None = None


@app.post('/api/users/user/create/')
def register_user(request:Request, user: UserSchemaCreate):
    user_crud = UserCrud('database.sqlite3')
    user_db = user_crud.get_user_tg(telegram_id=user.telegram_id)
    if user_db:
        return {"message": "user уже есть"}
    else:
        user_crud.add(username=user.username, password=user.password, telegram_id=user.telegram_id)
        return {"message": "ok"}




if __name__ == '__main__':
    create_table_database()
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)