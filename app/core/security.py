import jwt
from passlib.hash import scrypt
from datetime import timedelta, datetime
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.cofig import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/reg")


def hash_password(password: str) -> str:
    return scrypt.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return scrypt.verify(plain_password, hashed_password)


async def create_jwt(data: dict) -> str:
    data['exp'] = datetime.now() + timedelta(minutes=settings.EXP)
    return jwt.encode(payload=data, key=settings.SECRETKEY, algorithm=settings.ALGORITHM)


async def decode_jwt(token: str) -> dict:
    return jwt.decode(token, settings.SECRETKEY, algorithms=settings.ALGORITHM)


async def get_payload(token: str = Depends(oauth2_scheme)) -> dict:
    return await decode_jwt(token)

# async def create_refresh_token(data: dict) -> str:
