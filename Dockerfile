FROM python:3.8.1-slim

ENV PYTHONUNBUFFERED 1

EXPOSE $APP_PORT
WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY . ./

CMD ["mysql"]

# command to run on container start
CMD pip install -r requirements.txt && \
    python main.py