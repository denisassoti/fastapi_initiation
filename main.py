from fastapi import FastAPI
from app.routers import blog,user,authentication
from app import models, schemas
from app.settings.database import engine



app = FastAPI(
    title= "Denis @PI",
    version="1.0",
    docs_url="/",
    redoc_url="/docs",
    description="Initiation au framework fastapi et creation d'une api comportant l'autentification JWT"
)

models.Base.metadata.create_all(engine) # lancer les migrations dans la db





#include route
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)


