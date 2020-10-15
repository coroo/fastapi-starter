from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_hassing(plain_value, hashed_value):
    return pwd_context.verify(plain_value, hashed_value)


def create_hashing(value):
    return pwd_context.hash(value)
