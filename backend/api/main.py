from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# @app.get('/')
# async def root(): return {"message": "Hello World!"}
#uvicorn (file to run server)main:app --reload to load the server and making it reload for each change we do
#fastapi quickly creates a documentation of all the routes we create, and we can check then
# with Swagger through  http://127.0.0.1:8000/docs or Redocly through 
# http://127.0.0.1:8000/redocs
# @app.get('/next')
# async def root2(): return {"message": "Second route"}
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_db: [User] = [User(id= 1,name = "Maximiliano", surname = "Grosman", age = 29),
    User(id= 2,name = "Daniel Eduardo", surname = "Grosman", age = 61),
    User(id= 3,name= "Chapi", surname="Humara", age=12)]

#GET
@app.get('/users')
async def users():
    return users_db

#Param
@app.get("/user/{id}")
async def user_by_id(id: int):
    return search_user(id)

#Query
@app.get("/userQuery/")
async def user_by_query(id:int):
    return search_user(id)

def search_user(id: int):
    user = filter(lambda user: user.id == id, users_db)
    try: return list(user)[0]
    except: return {"error": "There wasn't an user with this ID"}

#POST
@app.post("/user/")
async def new_user(user: User):
    if type(search_user(user.id)) == User: return {"error": "It already exist"}
    else: 
        users_db.append(user)
        return {"message": "Created successfully"}

#PUT
@app.put("/user/")
async def update_user(user: User):
    if updated_user(user): return user
    return {"error": "Please send a valid user to update"}

def updated_user(user: User):
    found = False
    for i, to_Update in enumerate(users_db):
        if to_Update.id == user.id: found = True
        if found and to_Update.name != user.name: users_db[i].name = user.name
        if found and to_Update.surname != user.surname: users_db[i].surname = user.surname
        if found and to_Update.age != user.age: users_db[i].age = user.age
    return found

@app.delete('/user/{id}')
async def delete_user(id: int):
    for i, user in enumerate(users_db):
        if user.id == id:
            del users_db[i]
            found = True
            break
    if found: return {"message": "User successfully eliminated"}
    return {"error": "The user doesn't exist, please send a valid user"}