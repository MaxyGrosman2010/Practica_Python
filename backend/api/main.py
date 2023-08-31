from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root(): return {"message": "Hello World!"}
#uvicord main:app --reload to load the server and making it reload for each change we do