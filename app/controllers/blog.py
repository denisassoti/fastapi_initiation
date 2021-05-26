from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import APIRouter, Depends, status, Response, HTTPException


def get_all(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request : schemas.Blog, db : Session):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog) # add to database
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show(id : int, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Le blog avec l'id {id} n'existe pas")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Le blog avec l'id {id} n'existe pas"}
    return blog


def destroy(id : int, db : Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {"detail": "Le blog a ete suppimer avec succes"}


def update(id : int, request : schemas.Blog , db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Le blog avec l'id {id} n'existe pas")
    blog.update(title = request.title, body = request.body)
    db.commit()
    return "done"