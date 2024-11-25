from fastapi import FastAPI
from app.router import movie, auth,user

app=FastAPI()
app.include_router(movie.router)
app.include_router(auth.router)
app.include_router(user.router)

@app.get ("/")
def get_func():
    return "hello fastapi"