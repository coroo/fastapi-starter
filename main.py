import uvicorn
from typing import List

from fastapi import Depends, FastAPI, Header, HTTPException
from sqlalchemy.orm import Session

from app.middlewares import deps
from app.deliveries import items, users
from env import settings

app = FastAPI()


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