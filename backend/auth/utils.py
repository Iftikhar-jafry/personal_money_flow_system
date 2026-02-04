from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY="super-secret key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

#return hash of password
def hash_password(password:str)->str:
    return pwd_context.hash(password)


#verify the password
def verify_password(password:str,hash_password:str)->bool:
    return pwd_context.verify(password,hash_password)


#create token for access
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)
