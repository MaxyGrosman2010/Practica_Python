from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix='/users')

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_db: [User] = [User(id= 1,name = "Maximiliano", surname = "Grosman", age = 29),
    User(id= 2,name = "Daniel Eduardo", surname = "Grosman", age = 61),
    User(id= 3,name= "Chapi", surname="Humara", age=12)]

#GET
@router.get('/')
async def users():
    return users_db

#Param
@router.get("/{id}", response_model= User)
async def user_by_id(id: int):
    return search_user(id)

#Query
@router.get("/query")
async def user_by_query(id):
    return search_user(id)

def search_user(id: int):
    user = filter(lambda user: user.id == id, users_db)
    try: return list(user)[0]
    except: return {"error": "There wasn't an user with this ID"}

#POST
@router.post("/", response_model= User, status_code=201)
async def new_user(user: User):
    if type(search_user(user.id)) != User: 
        users_db.append(user)
        return users_db[-1]
    raise HTTPException(404, {"error": "It already exist"})

#PUT
@router.put("/", response_model= User)
async def update_user(user: User):
    if updated_user(user): return user
    raise HTTPException(404, {"error": "Please send a valid user to update"})

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
    if found: return {"message": "User successfully eliminated"}
    raise HTTPException(404, {"error": "The user doesn't exist, please send a valid user"})