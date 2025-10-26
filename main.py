from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel
app = FastAPI()

# Define a Pydantic model for post
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/posts")
async def get_posts():
    return {"data": "List of posts"}

@app.post("/createposts")
def create_post(new_post: Post):
    print(new_post.title)
    return {"data": "new post"}