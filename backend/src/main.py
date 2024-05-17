from fastapi import FastAPI, Request, status
from fastapi.responses import FileResponse
import uvicorn
from database import create_table_database
from orm import UserCrud
from music import search_and_download_music
from schemas import UserSchemaCreate, QueryMusicSchema

app = FastAPI(
    title="OpenMusic API"
)
user_crud = UserCrud('database.sqlite3')



@app.post('/api/music/download/')
def download_music(request: Request, query_music: QueryMusicSchema):
    if query_music.telegram_id:
        user = user_crud.get_user_tg(telegram_id=query_music.telegram_id)
    elif query_music.username:
        user = user_crud.get_user_web(username=query_music.username)
        print(user)
    file_name = search_and_download_music(query=query_music.query, username=user[1])
    if file_name:
        return FileResponse(path=file_name, media_type="audio", filename=file_name)


@app.post('/api/users/user/create/')
def register_user(request:Request, user: UserSchemaCreate):
    user_db = user_crud.get_user_tg(telegram_id=user.telegram_id)
    if user_db:
        return {"message": "user уже есть"}
    else:
        user_crud.add(username=user.username, password=user.password, telegram_id=user.telegram_id)
        return {"message": "ok"}







if __name__ == '__main__':
    create_table_database()
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)