from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
        return {"message": "Hello World"}

@app.get("/")
def getUserList():
    return user_dict
