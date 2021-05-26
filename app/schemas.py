from pydantic import BaseModel
from typing import List

## pydantic schema

class User(BaseModel):
    name : str
    email  : str
    password : str
    class Config():
        orm_mode = True


# class BlogCreator(BaseModel):
#     title : str
#     body : str
#     creator : User
#     class Config():
#         orm_mode = True 


class Blog(BaseModel):
    title : str
    body : str
    class Config():
        orm_mode = True
 

class ShowUser(BaseModel):
    name : str
    email  : str
    blogs : List[Blog] = []
    class Config():
        orm_mode = True


class ShowUserBlog(BaseModel):
    name : str
    email  : str
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title : str
    body : str
    creator : ShowUserBlog
    class Config():
        orm_mode = True # pour utiliser pydantic avec des orm


class Login(BaseModel):
    username  : str
    password : str
    class Config():
        orm_mode = True

