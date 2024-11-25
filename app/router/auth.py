from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from app.database import get_db
from app.model import User
from app.utils import verify_password
from app.oauth2 import create_access_token

router=APIRouter()
@router.post("/login")
def user_login(user:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    verify_user=db.query(User).filter(User.username==user.username).first()
    if not verify_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid user")
    if not verify_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid password")
    token=create_access_token({"user_id":verify_user.id})
    res = {
        "access_token":token,
        "token_type":"Bearer"
    }
    return res