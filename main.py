from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {"message": "welcome to my api"}

@app.get('/')
def get_posts():
    return {"data": "This is your post"}