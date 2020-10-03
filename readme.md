# Fast Api - Base Architecture

## Architecture
```bash
.
└── __pycache__             # Don't mind about me. I will auto generate if any changes only
└── app                     # I'm the app folder, that consist of
    ├── __pycache__             # Don't mind about me again :)
    ├── deliveries              # I'm a controller, but in here, you can call me delivery :)
    ├── middlewares             # I'm a cool middleware, don't me?
    ├── models                  # I will connecting you with your database structure
    ├── routers                 # Hi, you wanna post ? get ? Yes. Come at me :)
    ├── schemas                 # Don't you dare to ignore me. I will help your structure
    └── __init__.py             # In python, I will handle this sub-folder, so that you can easily calling them
└── main.py                 # Call me, then you will have your app running :3
└── readme.md               # You in me right now ;)
```

------

## Installation

Dependencies Installation
```console
pip3 install fastapi
pip3 install requests
pip3 install async-exit-stack async-generator
pip3 install sqlalchemy
```

Dependencies Unit Test
```console
pip3 install pytest
```

Dependencies Server Run
```console
pip3 install uvicorn
```

------

## Unit Test
```console
pytest
```

------

## Run App
```console
python3 main.py
```

## Documentation

Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 
Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

------

## Detail
For any X-Token Need, please use:
```
fake-super-secret-token
```
