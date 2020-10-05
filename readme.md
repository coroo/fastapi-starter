# Fast Api - Base Architecture 

[![ci](https://github.com/coroo/base-architecture/workflows/ci/badge.svg?branch=master)](../../actions)

:bulb: This architecture use the domain layer concept of [laravel](https://laravel.com/) from PHP, [rails](https://rubyonrails.org/) from Ruby and [clean-architecture](https://github.com/bxcodec/go-clean-arch#the-diagram) from Golang . By using this architecture, we hope that you don't need to create FastApi from sctrach again. Then you can focus on your development with our standardized pattern.

## :man_dancing: Architecture 
```python
.
|
└── app                     # I'm the app folder, that consist of:
    ├── deliveries              # I'm a controller with router, I will delivery your request :)
    ├── middlewares             # I'm a cool middleware, don't me?
    ├── models                  # I will connecting you with the database structure
    ├── repositories            # I'm a repositories, just like you ever know ;)
    ├── usecases                # Use me as services, so that you can create any usecases!
    ├── schemas                 # Don't you dare to ignore me. I will help all of data structure
    └── __init__.py             # In python, I will handle this sub-folder, so that you can easily calling them
└── config                  # Config anything ? Write on me then :D
    └── database.py             # You can do database configuration at me. Remember that!
    └── __init__.py             # Nice to meet you again!
└── test                    # Warning! You must create me (unit test) before ask them!
    └── {{all_unit_testing}}
    └── __init__.py             
└── env.py                  # I am the env.example, do you remember ?
└── main.py                 # Call me, then you will have your app running :3
└── readme.md               # You in me right now ;)
```

## :pushpin: Domain Layer
![diagram](https://github.com/bxcodec/go-clean-arch/raw/master/clean-arch.png)

------

## Installation

Add `.env` file with some value from [env.example](env.py)

## :rocket: Docker Installation
```
docker-compose up
```
Or see Manual Installation in [here](#manual-installation)

> For easily remove docker, you can use: docker-compose down

## :clipboard: Documentation

### Swagger

> Now go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
> You will see the automatic interactive API documentation (provided by Swagger UI)

### Alternative Documentation

> And now, go to [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).
> You will see the alternative automatic documentation (provided by ReDoc)

------

## Detail
For any X-Token Need, please use:
```
fake-super-secret-token
```

------

## Manual Installation

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
