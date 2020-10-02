# Fast Api - Base Architecture

## Architecture
```console
.
└── __pycache__
└── app
    ├── __pycache__
    ├── deliveries
    ├── middlewares
    ├── models
    ├── routers
    ├── schemas
    └── __init__.py
└── main.py
└── readme.md
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