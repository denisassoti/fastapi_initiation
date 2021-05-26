from fastapi import APIRouter, HTTPException, status, Depends
from app.settings import database
from app import schemas, models
from sqlalchemy.orm import Session
from app.settings.hashing import Hash




router = APIRouter(tags=['Authentification'])

@router.post('/login')
def login(request : schemas.Login, db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mot de passe incorrect")
    return user