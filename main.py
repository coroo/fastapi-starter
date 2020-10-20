import uvicorn
import logging
import os

from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.routers.api import api
from env import settings

from app.utils import metadata
from datetime import datetime

if not os.path.exists("storage"):
    os.mkdir("storage")
    if not os.path.exists("storage/logs"):
        os.mkdir("storage/logs")

log_filename = 'storage/logs/{:%Y-%m-%d}.log'.format(datetime.now())
logging.basicConfig(filename=log_filename, level=logging.ERROR,
                    format='%(asctime)s: [%(levelname)s] - %(message)s')

app = FastAPI(title=settings.APP_NAME,
              description=settings.APP_DESCRIPTION,
              version=settings.APP_VERSION,
              openapi_tags=metadata.tags)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=403, detail="Forbidden")

app.include_router(api, prefix=settings.API_PREFIX)


if __name__ == "__main__":
    if(settings.APP_MODE == 'development'):
        app_reload = True
    uvicorn.run(
        "main:app",
        log_level=settings.LOG_LEVEL,
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=app_reload)
