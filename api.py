"""
This is a new project for practice FastAPI
"""
from fastapi import FastAPI # import fastapi
from pydantic import BaseModel # import base model

app = FastAPI() #create fastapi instance

list_items = []


@app.get("/") # define path operation decorator
def hello_world():
    """
    Print hello world
    """
    
    return {"Hello": "World"}

@app.get("/item/{item_id}") # define path operation decorator
def hello_world(item_id:int):
    """
    path parameter
    """
    
    return {"item_id": item_id}


@app.post("/item") # define query operation decorator
def collect_items(item_name:str):
    """
    query parameter
    """
    list_items.append(item_name)
    return list_items

@app.get("/items/{item_id}") # define path operation decorator
def represnt_items(item_id:int) -> str:
    """
    path parameter-2
    Have all the items be displayed as per item number inthe list
    """
    return list_items[item_id]

