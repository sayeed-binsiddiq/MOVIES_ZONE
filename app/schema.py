
from pydantic import BaseModel
from typing import Optional

class Movie_base(BaseModel):
        title:str
        description:str

class Create_movie(BaseModel):
    title:str
    description:str
    year: int
   
class Update_movie(BaseModel):
    title:Optional[str]
    description:Optional[str]
    year:Optional[int]

class Movie_Response(Movie_base):
     id:int

class GenreBase(BaseModel):
     name:str
class GenreCreate(BaseModel):
     name:str


class GenreUpdate(BaseModel):
     name:str
class Genrereponse(BaseModel):
     name :str          

class UserBase(BaseModel):
     username:str
     password:str
class UserCreate(UserBase):
     pass
class Userupdate(UserBase):
     pass