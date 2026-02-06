from fastapi import APIRouter,HTTPException
import json
from auth.models import UserRegister,UserLogin
from auth.utils import hash_password,verify_password,create_access_token

router=APIRouter(prefix="/auth", tags=["Auth"])

USER_FILE="users.json"

def load_user():
    with open(USER_FILE,"r") as f:
        return json.load(f)

def save_user(users):
    with open(USER_FILE,"w") as f:
        json.dump(users,f,indent=4)

@router.post("/register")
def register(user:UserRegister):
    users=load_user()

    for u in users:
        if u["username"]==user.username:
            raise HTTPException(status_code=4000,detail="User already exist")
        
    users.append({
        "username":user.username,
        "hashed_password":hash_password(user.password)
    })

    save_user(users)
    return {"msg":"user registered successfully "}

@router.post("/login")
def login(user:UserLogin):
    users=load_user()
    for u in users:
        if u["username"]==user.username:
            if verify_password(user.password,u["hashed_password"]):
                token=create_access_token({"sub":user.username})
                return {"access_token":token,"token_type":"bearer"}
    
    raise HTTPException(status_code=401, detail="Invalid Credentials")
