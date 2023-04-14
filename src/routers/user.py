
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..Data.database import  get_db
from ..models import models
from .auth import *

user_router = APIRouter()

@user_router.post("/create/user")
async def create_user(user_dto: models.UserDto, db : Session = Depends(get_db)):
    user_model = models.Users()
    user_model.username = user_dto.username
    user_model.email = user_dto.email
    user_model.first_name = user_dto.first_name
    user_model.last_name = user_dto.last_name
    user_model.hashed_password = hash_password(user_dto.password)
    user_model.is_active = True

    db.add(user_model)
    db.commit()
    return {"Created": user_model.id}
    

@user_router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db :Session = Depends(get_db)):

    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    token_expires = timedelta(minutes=20)
    token = create_Access_token(user.username, user.id, expire_delta=token_expires)

    return token



