from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"message" : "Hello World!"}

@app.get("/users/{user}")
async def user(user: str):
    return {"user" : user}

@app.get("/items/")
async def item_name(item: str = None):
    if item == None:
        return {"items": "No"}
    else:
        return {"items": item}