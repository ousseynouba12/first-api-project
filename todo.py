from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI(title="TODO API", version="v1")

class Todo(BaseModel):
    name: str
    date: str
    description: str

# créons une liste

store_todo: [

]

@app.get("/")
async def home():
    return {"hello": "world"}

@app.post("/todo/")
async def create_todo(todo :Todo):
    
