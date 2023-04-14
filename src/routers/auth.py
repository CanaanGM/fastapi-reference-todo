from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import  Depends, HTTPException

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")
from dotenv import dotenv_values
from datetime import datetime, timedelta
from ..models import models

env_values = dotenv_values(".env")

async def get_current_user(token = Depends(oauth2_bearer)):
    try:

        payload = jwt.decode(token, env_values.get("SECRET_KEY"), env_values.get("ALGORITHM") )
        username = payload.get("sub")
        user_id = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(404, "no user")
    
        return {"username":username, "id":user_id}
    except JWTError :
        raise HTTPException(404, "no user")



def create_Access_token(username, userid, expire_delta = None):
    encode = {"sub":username, "id":userid}
    if expire_delta is not None:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    encode.update({"exp":expire})
    
    sk = env_values.get("SECRET_KEY")
    ag = env_values.get("ALGORITHM")
    return jwt.encode(encode, sk, ag)

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password) -> str:
    return bcrypt_context.hash(password)

def verify_pass(passwd, hashed_pass):
    return bcrypt_context.verify(passwd, hashed_pass)

def authenticate_user(username, passwd, db):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if not user : return False

    if not verify_pass(passwd, user.hashed_password): return False

    return user

