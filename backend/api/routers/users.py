from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix='/users')

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_db = {
    "maxtime": {"id": 1,"name": "Maximiliano Grosman", "age": 29, "username": "maxtime",
    "password":"$2a$12$WrFKfA3OSNMyV0M/nRdRROZyMnaxMcDSHqrPnWu6WHzn48SEuomnu", 
    "disable":False},
    "collector": {"id": 2, "name": "Daniel Eduardo Grosman", "age": 65,
    "username": "collector", 
    "password": "$2a$12$WrFKfA3OSNMyV0M/nRdRROZyMnaxMcDSHqrPnWu6WHzn48SEuomnu", 
    "disable": False}   
}

def search_user_id(id: int):
    user = filter(lambda user: user.id == id, users_db)
    try: return list(user)[0]
    except: return "There wasn't an user with this ID"

#GET
@router.get('/')
async def users():
    return users_db

#Param
@router.get("/{id}", response_model= User)
async def user_by_id(id):
    return search_user_id(id)

#Query
@router.get("")
async def user_by_query(id):
    int_id = int(id)
    return search_user_id(int_id)

#POST
@router.post("/", response_model= User, status_code=201)
async def new_user(user: User):
    if not type(search_user_id(user.id)) != User:
        raise HTTPException(404, detail= "It already exist")
    
    users_db.append(user)
    return users_db[-1]

#PUT
@router.put("/", response_model= User)
async def update_user(user: User):
    if not updated_user(user):
        raise HTTPException(404, detail= "Please send a valid user to update")
    
    return user

def updated_user(user: User):
    found = False
    
    for i, to_Update in enumerate(users_db):
        if to_Update.id == user.id: found = True
        if found and to_Update.name != user.name: users_db[i].name = user.name
        if found and to_Update.surname != user.surname: users_db[i].surname = user.surname
        if found and to_Update.age != user.age: users_db[i].age = user.age
    
    return found

@router.delete('/{id}')
async def delete_user(id: int):
    for i, user in enumerate(users_db):
        if user.id == id:
            del users_db[i]
            found = True
            break
    
    if not found:
        raise HTTPException(404, detail="The user doesn't exist, please send a valid user")
    
    return {"message": "User successfully eliminated"}