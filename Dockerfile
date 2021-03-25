FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

# EXPOSE $APP_PORT
WORKDIR /app


RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                mysql-dev \
                python3-dev \
                libffi-dev \
                openssl-dev \
        ;

RUN apk add build-base
RUN /usr/local/bin/python -m pip install --upgrade pip

COPY . ./

CMD ["mysql"]
CMD pip install alembic
CMD ["alembic","upgrade","head"]

# command to run on container start
CMD pip install -r requirements.txt && \
    pip install mysql-connector && \
    pip install alembic && \
    pip install pydantic[dotenv] && \
    pip install mysqlclient && \
    pip install passlib && \
    PYTHONPATH=. alembic upgrade head && \
    python main.py
