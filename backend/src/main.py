from fastapi import FastAPI
import uvicorn
from utils.database_table import create_table_database
from api.routers import all_routers

app = FastAPI(
    title="OpenMusic API"
)

for router in all_routers:
    app.include_router(router)


if __name__ == '__main__':
    create_table_database()
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)