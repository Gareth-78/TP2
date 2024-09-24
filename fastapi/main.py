from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool=None

@app.get("/")
def read_root():
    return {"Hello": "H3"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str=None):
    return {"item_id":item_id, "q":q}


@app.get("/gareth")
def read_gareth():
    return{"name":"Gareth"}