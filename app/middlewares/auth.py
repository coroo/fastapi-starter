from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from env import settings
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from sqlalchemy.orm import Session
from app.middlewares.deps import get_db
from app.schemas.user_schema import User
from app.schemas.token_schema import TokenData
from app.utils.hash import verify_hassing
from app.usecases import user_usecase

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "e1bace6f2c07af745841d5cfee6c65fa2dae73655ca0d0d026dc8ec5939dafb2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.API_PREFIX+"/users/token")
    

def authenticate_user(db, email: str, password: str):
    user = user_usecase.get_user_by_email(db, email)
    if not user:
        return False
    if not verify_hassing(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
            token: str = Depends(oauth2_scheme), 
            db: Session = Depends(get_db)
        ):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    print(token_data.email)
    user = user_usecase.get_user_by_email(db, email=token_data.email)
    print("SAYA DSINI")
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
            current_user: User = Depends(get_current_user)
        ):
    if current_user.is_active != 1:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
