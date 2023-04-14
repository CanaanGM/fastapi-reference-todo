from fastapi import FastAPI

from .routers import todos, user

routers = [todos.todo_router, user.user_router]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Canaan again teice!"}


for router in routers:
    app.include_router(router)
