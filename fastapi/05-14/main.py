from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/items/{item}")
async def root(item: int = Path(..., ge=1, le=1000), q: str = Query( default=None, min_length=3, max_length=10, regex="^[a-zA-Z0-9?!_]*$")):
    return {"item":f"{item} {q}"}

class Item_Model(BaseModel):
    name: str = Field(..., min_length=3, max_length=1000)
    description: str
    price: int = Field(..., gt=1000, le=100000)
    tax: float
    imgs: list[str]

class ItemStar(BaseModel):
    star: int
    comment: str

@app.post("/shop")
async def shop(item: Item_Model, star: ItemStar):
    return item, star

class Find(BaseModel):
    name: str
    type: str

class Loc(BaseModel):
    name: str
    type: str
    msg: str

@app.post("/find_my")
async def loc(find: Find) -> Loc:
    if find.name == "EGL":
        msg = "춘식이 호출번호는 010-xxxx-xxx"
        type = "기만자"
        name = find.name
    else:
        msg = "찾는중 남은시간: 9999d"
        type = find.type
        name = find.name
    return Loc(name=name, type=type, msg=msg)