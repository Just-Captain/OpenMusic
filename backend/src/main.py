from fastapi import FastAPI, Request
import uvicorn

app = FastAPI(
    title="OpenMusic API"
)


@app.get('/')
def message(request: Request):
    print(request)
    return {"message": "Hello user"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)