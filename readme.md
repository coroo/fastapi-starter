# Fast Api - Base Architecture 
![ci](https://github.com/coroo/base-architecture/workflows/ci/badge.svg?branch=master)

## Architecture 
```python
.
|
└── app                     # I'm the app folder, that consist of:
    ├── deliveries              # I'm a controller, but in here, you can call me delivery :)
    ├── middlewares             # I'm a cool middleware, don't me?
    ├── models                  # I will connecting you with your database structure
    ├── routers                 # Hi, you wanna post ? get ? Yes. Come at me :)
    ├── schemas                 # Don't you dare to ignore me. I will help your structure
    └── __init__.py             # In python, I will handle this sub-folder, so that you can easily calling them
└── config                  # Config anything ? Write on me then :D
    └── database.py             # You can do database configuration at me. Remember that!
    └── __init__.py             # Nice to meet you again!
└── test                    # Warning! You must create me (unit test) before ask them!
    └── all-unit-testing
    └── __init__.py             
└── env.py                  # I am the env.example, do you remember ?
└── main.py                 # Call me, then you will have your app running :3
└── readme.md               # You in me right now ;)
```

------

## Docker Installation
```
docker-compose up
```
Or see Manual Installation in [here](#installation)

> For easily remove docker, you can use: docker-compose down

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

------

## Installation

Dependencies Installation
```console
pip3 install fastapi
pip3 install requests
pip3 install async-exit-stack async-generator
pip3 install python-dotenv
pip3 install sqlalchemy
pip3 install pymysql
```

Dependencies Unit Test
```console
pip3 install pytest
```

Dependencies Server Run
```console
pip3 install uvicorn
```
