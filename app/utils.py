from passlib.context import CryptContext
pwd=CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash_password(plain):
    return pwd.hash(plain)
def verify_password(plain,hashed):
    return pwd.verify(secret=plain,hash=hashed)
