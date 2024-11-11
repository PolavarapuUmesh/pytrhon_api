from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserStatus(BaseModel):
    id: int
    status: str

users = [
    {"id": 1, "status": "active"},
    {"id": 2, "status": "inactive"},
    {"id": 3, "status": "pending"},
]

@app.get("/users/")
async def read_users():
    return users

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/")
async def create_user(user: UserStatus):
    users.append(user.dict())
    return user

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UserStatus):
    for i, u in enumerate(users):
        if u["id"] == user_id:
            users[i] = user.dict()
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u["id"] == user_id:
            del users[i]
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")