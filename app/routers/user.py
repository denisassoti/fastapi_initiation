from app import models, schemas
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.settings import database
from app.controllers import user



router = APIRouter(prefix='/user', tags=['User'])


# user routes

@router.post('/', response_model=schemas.ShowUser)
def create_user(request : schemas.User, db : Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(id : int,db : Session = Depends(database.get_db)):
    return user.show(id,db)