# auth/dependencies.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from auth.utils import SECRET_KEY, ALGORITHM
from auth.routes import load_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    print(token)
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username=payload.get("sub")
        users=load_user()
        if not any(u["username"]==username for u in users):
            raise HTTPException(status_code=400,detail="User not found")
        return username
    except:
        raise HTTPException(status_code=401,detail="Invalid Token")