from fastapi import APIRouter, Depends, HTTPException,status,Response
from sqlalchemy.orm.session import Session
from app.schema import Movie_Response,Create_movie,Update_movie,GenreCreate,Genrereponse,GenreUpdate
from app.database import get_db
from app.model import Movie,Genre
from app.oauth2 import get_current_user
from typing import List
router= APIRouter()
@router.get("/movie",response_model=List[Movie_Response])
def get_movie(db:Session=Depends(get_db)):
    movies= db.query(Movie).all()
    return movies

@router.post("/movie",response_model=Movie_Response)
def create_movie(movie:Create_movie,db:Session=Depends(get_db), current_user=Depends(get_current_user)):
    new_movie=Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

@router.put ("/movie/{id}")
def update_movie(id:int,movie:Update_movie,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    update_movie=db.query(Movie).filter(Movie.id==id)
    to_update=update_movie.first()
    if not to_update:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,details="movie is not found")
    update_movie.update(movie.dict(),synchronize_session=False)
    db.commit()
    db.refresh(to_update)
    return to_update

@router.delete("/movie/{id}")
def delete_movie(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    delete_query=db.query(Movie).filter(Movie.id==id)
    to_delete=delete_query.first()
    if not to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="movies is not found")
    delete_query.delete()
    db.commit()
    return f"your movie is delete successfully"

@router.get("/genres")
def get_genre(db:Session=Depends(get_db)):
    genres=db.query(Genre).all()
    return genres

@router.post("/genres")
def create_genre(genre:GenreCreate,db:Session=Depends(get_db)):
    new_genre=Genre(name=genre.name)
    db.add(new_genre)
    db.commit()
    db.refresh(new_genre)
    return new_genre

@router.put("/genres/{id}")
def update_genre(id:int,genre:GenreUpdate,db:Session=Depends(get_db)):
    update_query=db.query(Genre).filter(Genre.id==id)
    to_update=update_query.first()
    if not to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="genre is not found")
    update_query.update(genre.dict(),synchronize_session=False)     
    db.commit()
    db.refresh(to_update)
    return to_update

@router.delete("/genres/{id}")
def delete_genre(id:int,db:Session=Depends(get_db)):
    delete_query=db.query(Genre).filter(Genre.id==id)
    to_delete=delete_query.first()
    if not to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="genre is not found")
    delete_query.delete()
    db.commit()
    return f"genre is successfully deleted"

