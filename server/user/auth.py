from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from pydantic import EmailStr

from user.dao import UserDAO
from config import settings



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = settings.secret_key_for_jwt
ALGORITHM = settings.algorithm_for_jwt

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=3)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def authenticate_user(namespace: str, password: str):
    user = await UserDAO.find_one_or_none(email=namespace)

    if not user:
        user = await UserDAO.find_one_or_none(nickname=namespace)

    if not user or not verify_password(password, user.password):
        return None

    return user