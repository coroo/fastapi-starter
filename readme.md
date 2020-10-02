### Fast Api - Base Architecture

Dependencies Installation
```
pip3 install fastapi
pip3 install requests
pip3 install async-exit-stack async-generator
pip3 install sqlalchemy
```
Dependencies Server Run
```
pip3 install uvicorn #(recommendation)
or
pip3 install hypercorn
```

------

### Run App
```
uvicorn main:app --reload #(recommendation)
or
hypercorn main:app --reload
```
### Run Swagger

Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or another documentation at [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

------

### Detail
For any X-Token Need, please use:
```
fake-super-secret-token
```