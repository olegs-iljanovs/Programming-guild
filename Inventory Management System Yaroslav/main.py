from fastapi import FastAPI, HTTPException, status, Query, Response
from pydantic import BaseModel
from random import randrange

app = FastAPI()
inventory = [
    {"id": 1, "name": "Apple", "quantity": 2},
]

class Product(BaseModel):
    name: str
    quantity: int

def find_index_post(id):
    for i, p in enumerate(inventory):
        if p["id"] == id:
            return i


@app.get("/inventory")
def get_inventory():
    return inventory

@app.post("/product", status_code=status.HTTP_201_CREATED)
def create_post(item: Product):
    item_dict = item.dict()
    if item_dict["quantity"] <= 0:
        raise HTTPException(status_code=418,
                            detail=f"Quantity can't be below 1")
    item_dict["id"] = randrange(0, 1000000)
    inventory.append(item_dict)
    return {"data": item_dict}

@app.delete("/inventory/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with ID {id} does not exist")
    inventory.pop(index)
    return {"message": f"Product with ID {id} successfully deleted"}

@app.put("/posts/{id}")
def update_post(id: int, item: Product):
    indx = find_index_post(id)
    if indx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with ID {id} does not exist")
    item_dict = item.dict()
    item_dict["id"] = id
    inventory[indx] = item_dict
    return {"message": f"Product with ID {id} successfully updated"}