from api.musics import router as router_musics
from api.users import router as router_users
from api.urls import router as urls_template


all_routers = [
    router_musics,
    router_users,
    urls_template
]