from app import models, schemas
from app.settings import oauth2
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.settings.hashing import Hash
from app.settings import database
from app.controllers import blog
from app.settings.oauth2 import get_current_user

router = APIRouter(prefix='/blog', tags=['Blog'])



# blog routes

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog, db : Session = Depends(database.get_db), current_user : schemas.User = Depends(get_current_user)):
    return blog.create(request, db)

#current_user : schemas.User = Depends(get_current_user) for make middleware
@router.get('/', response_model=List[schemas.ShowBlog])
def list(db : Session = Depends(database.get_db), current_user : schemas.User = Depends(get_current_user)): # middleware
    return blog.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id : int,db : Session = Depends(database.get_db), current_user : schemas.User = Depends(get_current_user)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id : int, db : Session = Depends(database.get_db), current_user : schemas.User = Depends(get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id : int, request : schemas.Blog, db : Session = Depends(database.get_db), current_user : schemas.User = Depends(get_current_user)):
    return blog.update(id, request, db)
