from app.settings.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date,time

## sqlalchemy models for database

class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('user.id')) 
    creator = relationship("User", back_populates = "blogs")


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship("Blog", back_populates = "creator")


# Cinema Models

# class Ville(Base):
#     __tablename__ = 'ville'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)


# class Cinema(Base):
#     __tablename__ = 'cinema'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     nombreSalles = Column(Integer)


# class Salle(Base):
#     __tablename__ = 'salle'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     nombrePlaces = Column(Integer)


# class Categorie(Base):
#     __tablename__ = 'categorie'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)


# class Film(Base):
#     __tablename__ = 'film'

#     id = Column(Integer, primary_key=True, index=True)
#     titre = Column(String)
#     duree = Column(float)
#     realisateur = Column(String)
#     description = Column(String)
#     photo = Column(String)
#     dateSortie = Column(date)



# class Place(Base):
#     __tablename__ = 'place'

#     id = Column(Integer, primary_key=True, index=True)
#     numero = Column(Integer)


# class Seance(Base):
#     __tablename__ = 'seance'

#     id = Column(Integer, primary_key=True, index=True)
#     heureDebut = Column(time)


# class Ticket(Base):
#     __tablename__ = 'ticket'

#     id = Column(Integer, primary_key=True, index=True)
#     nomClient = Column(String)
#     prix = Column(float)
#     codePaiement = Column(int)
#     reserve = Column(bool)