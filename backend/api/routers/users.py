from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix='/users', tags=["auth"], 
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})

def search_user(field: str, key):
    try: return User(**user_schema(db_client.local.users.find_one({field: key})))
    except: return "There isn't an user list that"

#GET
@router.get('/', response_model=list[User])
async def users():
    return users_schema(db_client.local.users.find())

#Param
@router.get("/{id}", response_model= User)
async def user_by_id(id: str):
    return search_user("_id", id)

#Query
@router.get("")
async def user_by_query(id: str):
    return search_user("_id", ObjectId(id))

#POST
@router.post("/", response_model= User, status_code=status.HTTP_201_CREATED)
async def new_user(user: User):
    if not type(search_user("email", user.email)) != User:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "It already exist")
    
    user_dict = dict(user)
    del user_dict["id"]#Making sure MongoDB creates the id
    id = db_client.local.users.insert_one(user_dict).inserted_id

    return User(**user_schema(db_client.local.users.find_one({"_id": id})))

#PUT
@router.put("/", response_model= User)
async def update_user(user: User):
    user_dict = user
    del user_dict["id"]

    try: User(**user_schema(db_client.local.users
        .find_one_and_replace({"_id": ObjectId(user.id)},user_dict)))
    except: raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Invalid data")

    return search_user("_id", ObjectId(user.id))

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):

    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found: raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
        detail="User not found")
    return {"message": "Success"}