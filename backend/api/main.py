from fastapi import FastAPI
from routers import users

app = FastAPI()

#uvicorn (file to run server)main:app --reload to load the server and making it reload for each change we do
#fastapi quickly creates a documentation of all the routes we create, and we can check then
# with Swagger through  http://127.0.0.1:8000/docs or Redocly through 
# http://127.0.0.1:8000/redocs

app.include_router(router= users.router,)