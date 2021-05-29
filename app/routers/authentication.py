from fastapi import APIRouter, HTTPException, status, Depends
from app.settings import database
from app import schemas, models
from sqlalchemy.orm import Session
from app.settings.hashing import Hash
from datetime import datetime, timedelta
from app.settings.Jwt_token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from app.controllers import authentication



router = APIRouter(tags=['Authentification'])

@router.post('/login')
def login(request : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(database.get_db)):
    # user = db.query(models.User).filter(models.User.email == request.username).first()
    # if not user : 
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    # if not Hash.verify(user.password,request.password):
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mot de passe incorrect")

    # access_token = create_access_token(data={"sub": user.email})
    # return {"access_token": access_token, "token_type": "bearer"}
    return authentication.login(request, db)