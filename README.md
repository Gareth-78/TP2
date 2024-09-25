# Run a FastAPI "Hello World" Python app into a container

## main.py:
```
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

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```
## fastapi.dockerfile:
```
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

COPY ./app /app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

### docker ps
![Capture d’écran du 2024-09-25 14-21-06](https://github.com/user-attachments/assets/b0eea725-2a92-4588-bcfa-b013d4587afd)
### fastapi/docs
![Capture d’écran du 2024-09-25 14-26-50](https://github.com/user-attachments/assets/28c59f9c-fc7c-478d-9421-e53b7706a026)
