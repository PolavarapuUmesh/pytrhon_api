import secrets
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserInfo(BaseModel):
    username: str
    password: str

@app.post("/store")
async def store_user_info(user_info: UserInfo):
    with open('user_info.txt', 'a') as file:
        file.write(f"Username: {user_info.username}, Password: {user_info.password}\n")

    return {"message": "User info stored successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

pass_length=12
print(secrets.token_bytes(pass_length))