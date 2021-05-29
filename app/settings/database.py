from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv, find_dotenv
import urllib

#recuperation des variables d'env du ficgier .env
load_dotenv(find_dotenv()) 


#print(os.getenv('DB_CONNECTION','hh'))

## config de base de donnees modulaire
# permet de gerer les types de bases de donnees plus facilement en fonction des variables d'environnement

#recuperation des variables
db_connection = os.getenv('DB_CONNECTION') 
host_server = os.getenv('DB_HOST')
db_server_port = urllib.parse.quote_plus(str(os.getenv('DB_PORT')))
database_name = os.getenv('DB_DATABASE')
db_username = urllib.parse.quote_plus(str(os.getenv('DB_USERNAME')))
db_password = urllib.parse.quote_plus(str(os.getenv('DB_PASSWORD')))
ssl_mode = urllib.parse.quote_plus(str(os.getenv('SSL_MODE','prefer')))


SQLALCHEMY_DATABASE_URL = None
init_engine = None

if(db_connection.__len__ == 0 or db_connection == 'sqlite'):
    SQLALCHEMY_DATABASE_URL  = 'sqlite:///./database.db'
    init_engine= create_engine(
        SQLALCHEMY_DATABASE_URL,connect_args = {"check_same_thread": False}
    )
elif(db_connection == 'postgresql'):
    SQLALCHEMY_DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
    #SQLALCHEMY_DATABASE_URL = 'postgresql://tdvzdfuqamhgrv:ffdf3ccf930407d55aa795af4a565ad6189dbeea850e823357b9ec140f3be197@ec2-184-73-198-174.compute-1.amazonaws.com:5432/d5grfku45ar20l'
    init_engine = create_engine(
        SQLALCHEMY_DATABASE_URL, pool_size = 3, max_overflow = 0 
    )
elif(db_connection == 'mysql'):
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(db_username, db_password, host_server, db_server_port, database_name)
    init_engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
elif(db_connection == 'mongodb'):
    pass


#postgres://tdvzdfuqamhgrv:ffdf3ccf930407d55aa795af4a565ad6189dbeea850e823357b9ec140f3be197@ec2-184-73-198-174.compute-1.amazonaws.com:5432/d5grfku45ar20l



engine = init_engine


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()