from sqlalchemy import Column, Integer,String
from app.database import Base

class Movie(Base):
    __tablename__="movies"
    id= Column(Integer, primary_key=True)
    title=Column(String,nullable=True)
    description =Column(String)
    year=Column(Integer)

class Genre(Base):
    __tablename__="genres"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False,unique=True)
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    username=Column(String ,nullable=False,unique=True)
    password=Column(String,nullable=False)  


