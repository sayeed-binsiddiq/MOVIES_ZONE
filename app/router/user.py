from fastapi import FastAPI,APIRouter,Depends
from sqlalchemy.orm.session import Session
from app.database import get_db
from app.schema import UserCreate
from app.model import User
from app.utils import hash_password
router=APIRouter()
@router.post("/user")
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    user.password = hash_password(user.password)
    new_user= User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user