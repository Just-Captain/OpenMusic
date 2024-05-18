from http.client import HTTPException

from fastapi import APIRouter, Request

from orm.users import UserCrud
from schemas.users import UserRegisterSchema, UserLoginSchema

user_crud = UserCrud('database.sqlite3')


router = APIRouter()

@router.post('/api/auth/user/register/')
def register_user(request:Request, new_user: UserRegisterSchema):
    user = user_crud.create_user(
        username=new_user.username,
        password=new_user.password,
        telegram_id=new_user.telegram_id
    )
    return {'message': 'User created successfully'}


@router.post('/api/auth/user/login/')
def login_user(request:Request, new_user: UserLoginSchema):
    pass

@router.get('/api/users/user/get/')
def get_user(
        request:Request,
        user_id: int | None = None,
        username: str | None = None,
        telegram_id: str | None = None
) -> dict:
    user = user_crud.get(user_id, username, telegram_id)
    if user is None:
        return {'message': 'user does not exist'}
    return user.to_dict()

@router.get('/api/users/all/')
def get_all_users(
        request:Request,
) -> dict:
    users = user_crud.all()
    print(users)
    return users