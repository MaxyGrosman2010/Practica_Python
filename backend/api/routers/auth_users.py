from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth", tags=["auth"], 
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})
oauth = OAuth2PasswordBearer(tokenUrl="login")
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 60
crypt = CryptContext(schemes=["bcrypt"])
SECRET = "38d084ef4c8926791dffcc2a82116f6778bddd08ee8e4d9d149c341ea37e37f4"

class User(BaseModel):
    id: int
    name: str
    username: str
    age: int
    disable: bool

class UserDB(User):
    password: str

users_db = {
    "maxtime": {"id": 1,"name": "Maximiliano Grosman", "age": 29, "username": "maxtime",
    "password":"$2a$12$ynLbOul1BAXJ29MO5lZ6fe/Qdh3SQ6gVmoxQ9h5gaQEcG1Aj9TTsm", 
    "disable":False},
    "collector": {"id": 2, "name": "Daniel Eduardo Grosman", "age": 65,
    "username": "collector", 
    "password": "$2a$12$ynLbOul1BAXJ29MO5lZ6fe/Qdh3SQ6gVmoxQ9h5gaQEcG1Aj9TTsm", 
    "disable": False}   
}

#Install pip install "python-jose[cryptography]" and pip install "passlib[bcrypt]" for jwt
#To generate a random secret key: openssl rand -hex 32

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

async def auth_user(token: str = Depends(oauth)):
    exception = HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
    detail= "Invalid credentials user")
    
    try: 
        username = jwt.decode(token, SECRET, algorithms= ALGORITHM).get("sub")
        if username is None: raise exception
    except JWTError: raise exception

    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    if user.disable:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
        detail= "Inactive user")
    
    return user



@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db: 
        raise HTTPException(status_code=400, detail= "User is not valid")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail= "Password is not valid")
    
    if user.disable:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail= "Inactive user")
    
    access_token = {"sub": user.username, 
    "exp": datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_DURATION)}
    
    return {"access_token": jwt.encode(access_token, SECRET,
        algorithm= ALGORITHM),
    "token_type": "Bearer"}

@router.get("/me")
async def me(user: User = Depends(current_user)):
    return user