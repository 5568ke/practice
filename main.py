from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_dict={}

Class User(BaseModel):
    id : str
    name : str

@app.get("/")
async def root():
        return {"message": "Hello World"}

@app.get("/")
def getUserList():
    return user_dict

@app.post("/register")
def register(user : User):
    user_dict[user.id]=user.name
    
