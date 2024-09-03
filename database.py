from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
 
 #crear camino de la base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./usuarios"
 
# Crear el motor para la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})
 
# Crear la Sesion Local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()


