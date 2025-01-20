from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel
import random

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza.", "id": 2}]

@app.get('/posts')
def get_posts():
    return {"posts": my_posts}

@app.get('/')
def home():
    return {"MESSAGE": "Welcome to my Test API"}

@app.post("/posts")
def create_posts(post: Post):
    new_post = post.dict()
    new_post['id'] = random.randint(1,100000000000)
    my_posts.append(new_post)
    return {"SUCCESS": new_post}
#title, str and content, str
