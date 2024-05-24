# OpenMusic

Проект OpenMusic написан студентами академии ТОП в качестве лабораторной работы.

## Технологии
[Language - Python, version 3.12](https://www.python.org/)
<p align="center">
    <a href="https://fastapi.tiagolo.com"><img src="https://www.python.org/static/img/python-logo.png">
</p>

[Framework - FastApi](https://fastapi.tiangolo.com/) <p align="center">
    <a href="https://fastapi.tiagolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png">
</p>

[Core lib - Pytube](https://pytube.io/en/latest/) <p align="center">
    <a href="https://fastapi.tiagolo.com"><img src="https://camo.githubusercontent.com/77e56082aa1f10ddd2ccf0d2c0c5b3d0d549a8b6e0650735ee0781c72024417a/68747470733a2f2f6173736574732e6e69636b666963616e6f2e636f6d2f67682d7079747562652e6d696e2e737667">
</p>


## Установка
Windows:
```bash
python -m venv venv
.venv\Scripts\activate
pip install requirements.txt
```
Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install requrements.txt
```
## Запуск
```bash
cd src
python main.py
```
### Консоль
```console
╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/backend/src/']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Interactive API docs

Now go to <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Alternative API docs

And now, go to <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)


## License
[MIT](https://choosealicense.com/licenses/mit)