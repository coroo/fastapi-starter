from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status, Security
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey

from env import settings
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from sqlalchemy.orm import Session
from app.middlewares.deps import get_db
from app.middlewares import deps, di
from app.schemas.user_schema import User
from app.schemas.token_schema import TokenData
from app.utils.hash import verify_hassing
from app.usecases.user_service import UserService
from app.schemas import user_schema, token_schema


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

API_KEY = "1234567asdfgh"
API_KEY_NAME = "Authorization"

bearer = 'Bearer '

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl=settings.API_PREFIX+"/users/token"
    )

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def authenticate_user(db, email: str, password: str):
    user = UserService.read_by_email(db, email)
    if not user:
        return False
    if not verify_hassing(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
            token: Optional[str] = Security(api_key_header),
            db: Session = Depends(get_db),
            commons: dict = Depends(di.common_parameters),
            active: bool = True,
        ):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    if token is None:
        raise credentials_exception
        pass
    else:
        split_token = token.rsplit(' ')

        if split_token[0] != 'Bearer':
            user = UserService.read(db, user_id=split_token[0])
            if user is not None:
                if user.id == token:
                    return user
                else:
                    raise credentials_exception
                    pass
                pass
            else:
                raise credentials_exception
                pass
        else:
            if len(split_token) > 1:
                try:
                    payload = jwt.decode(split_token[1], SECRET_KEY, algorithms=[ALGORITHM])
                    email: str = payload.get("sub")
                    if email is None:
                        raise credentials_exception
                    token_data = TokenData(email=email)
                except JWTError:
                    raise credentials_exception
                user = UserService.read_by_email(db, email=token_data.email)
                if user is None:
                    raise credentials_exception
                else:
                    if user.email == token_data.email:
                        return user
                    else:
                        raise credentials_exception
                        pass
                pass
            else:
                raise credentials_exception
                pass
    pass

    
async def get_current_active_user(
            current_user: User = Depends(get_current_user)
        ):
    if current_user.is_active != 1:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user