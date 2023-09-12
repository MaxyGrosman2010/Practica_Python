from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    name: str
    surname: str
    username: str
    email: str
    age: int

class UserDB(User):
    password: str
    disable: Optional[bool] = False