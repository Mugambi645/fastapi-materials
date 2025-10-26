from fastapi import FastAPI, Body
from pydantic import BaseModel
app = FastAPI()

# Define a Pydantic model for post
class Post(BaseModel):
    title: str
    content: str


@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/posts")
async def get_posts():
    return {"data": "List of posts"}

@app.post("/createposts")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"new post": f"title {payload[title]} {payload[content]}"}