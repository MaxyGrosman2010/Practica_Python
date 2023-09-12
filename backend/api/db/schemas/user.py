def user_schema(user) -> dict:
    return {"id": str(user["_id"]), "name": user["name"], "surname": user["surname"],
    "username": user["username"], "email": user["email"], "age": user["age"]}

def users_schema(users) -> list:
    return  [user_schema(user) for user in users]

def userdb_schema(user) -> dict:
    return {"id": str(user["_id"]), "name": user["name"], "surname": user["surname"],
    "username": user["username"], "email": user["email"], "age": user["age"],
    "password": user["password"], "disable": user["disable"]}