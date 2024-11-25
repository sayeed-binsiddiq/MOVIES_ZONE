from datetime import datetime,timedelta
from fastapi import HTTPException,Depends,status
from sqlalchemy.orm.session import Session
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from app.config import settings
from app.database import get_db
from jose import jwt,JWTError
from app.model import User

SECRET_KEY=settings.SECRET_KEY
ALOGRITHM=settings.ALOGRITHM
ACCESS_EXPIRSE_TIME=settings.ACCESS_EXPIRSE_TIME
Oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_EXPIRSE_TIME)
    to_encode.update({"exp":expire})
    token=jwt.encode(to_encode,SECRET_KEY,ALOGRITHM)
    return token

def verify_access_token(token:str, credential_exception):
    try:
        token_data=jwt.decode(token,SECRET_KEY,algorithms=[ALOGRITHM])
        user_id=token_data.get("user_id")
        if not user_id:
            raise credential_exception
    except:
        if not JWTError:
          raise credential_exception
        return user_id
    

def get_current_user(token:str=Depends(Oauth2_scheme),db:Session=Depends(get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="user is not found")
    user_id=verify_access_token(token, credential_exception)
    current_user=db.query(User).filter(User.id==user_id).first()
    return current_user