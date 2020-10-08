import uvicorn
from typing import List

from fastapi import Depends, FastAPI, Header, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.middlewares import deps
from app.deliveries import items, users
from env import settings

# CREATE LOGS DIRECTORY
import os
if not os.path.exists('logs'):
    os.makedirs('logs')

app = FastAPI()

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


app.include_router(users.router, prefix=settings.API_PREFIX)
app.include_router(
    items.router,
    prefix=settings.API_PREFIX,
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
