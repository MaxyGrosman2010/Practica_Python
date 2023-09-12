from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from db.models.user import UserDB, User
from db.schemas.user import userdb_schema
from db.client import db_client
from datetime import datetime, timedelta


router = APIRouter(prefix="/auth", tags=["auth"], 
responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})
oauth = OAuth2PasswordBearer(tokenUrl="login")
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 60
crypt = CryptContext(schemes=["bcrypt"])
SECRET = "38d084ef4c8926791dffcc2a82116f6778bddd08ee8e4d9d149c341ea37e37f4"

#Install pip install "python-jose[cryptography]" and pip install "passlib[bcrypt]" for jwt
#To generate a random secret key: openssl rand -hex 32

def search_user(field: str, key):
    try: return UserDB(**userdb_schema(db_client.users.find_one({field: key})))
    except: return "Not found"

async def auth_user(token: str = Depends(oauth)):
    exception = HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
    detail= "Invalid credentials user")
    
    try: 
        username = jwt.decode(token, SECRET, algorithms= ALGORITHM).get("sub")
        if username is None: raise exception
    except JWTError: raise exception

    return search_user("username",username)

async def current_user(user: UserDB = Depends(auth_user)):
    if user.disable:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
        detail= "Inactive user")
    
    return User(**user)

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = search_user("username", form.username)
    if user_db == "Not found": 
        raise HTTPException(status_code=400, detail= "User is not valid")
    
    if not crypt.verify(form.password, user_db.password):
        raise HTTPException(status_code=400, detail= "Password is not valid")
    
    if user_db.disable:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail= "Inactive user")
    
    access_token = {"sub": user_db.username, 
    "exp": datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_DURATION)}
    
    return {"access_token": jwt.encode(access_token, SECRET,
        algorithm= ALGORITHM),
    "token_type": "Bearer"}

@router.get("/me")
async def me(user: User = Depends(current_user)):
    return User(**user)