from fastapi import APIRouter, Request
from schemas.musics import QueryMusicSchema
from orm.users import UserCrud
from utils.download_music import search_and_download_music
from fastapi.responses import FileResponse

router = APIRouter()
user_crud = UserCrud('database.sqlite3')

@router.post('/api/music/download/')
def download_music(request: Request, query_music: QueryMusicSchema):
    if query_music.telegram_id:
        user = user_crud.get_user_tg(telegram_id=query_music.telegram_id)
    elif query_music.username:
        user = user_crud.get_user_web(username=query_music.username)
        print(user)
    file_name = search_and_download_music(query=query_music.query, username=user[1])
    if file_name:
        return FileResponse(path=file_name, media_type="audio", filename=file_name)
