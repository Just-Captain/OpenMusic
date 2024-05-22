from fastapi import APIRouter, Request
from schemas.users import UserSchemaCreate
from orm.users import UserCrud

router = APIRouter()
user_crud = UserCrud('database.sqlite3')



@router.post('/api/users/user/create/')
def register_user(request:Request, user: UserSchemaCreate):
    user_db = user_crud.get_user_tg(telegram_id=user.telegram_id)
    if user_db:
        return {"message": "user уже есть"}
    else:
        user_crud.add(username=user.username, password=user.password, telegram_id=user.telegram_id)
        return {"message": "ok"}