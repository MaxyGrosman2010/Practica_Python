from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root(): return {"message": "Hello World!"}
#uvicorn main:app --reload to load the server and making it reload for each change we do
#fastapi quickly creates a documentation of all the routes we create, and we can check then
#through  http://127.0.0.1:8000/docs
@app.get('/next')
async def root2(): return {"message": "Second route"}