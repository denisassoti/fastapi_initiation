from app import models, schemas
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.settings.hashing import Hash
from app.settings import database
from app.controllers import blog

router = APIRouter(prefix='/blog', tags=['Blog'])



# blog routes

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog, db : Session = Depends(database.get_db)):
    return blog.create(request, db)


@router.get('/', response_model=List[schemas.ShowBlog])
def list(db : Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id : int,db : Session = Depends(database.get_db)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id : int, db : Session = Depends(database.get_db)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id : int, request : schemas.Blog, db : Session = Depends(database.get_db)):
    return blog.update(id, request, db)
