from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Dict
import bcrypt

app = FastAPI()

users_db: Dict[str, Dict] = {}


class UserRegistration(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class TranslationRequest(BaseModel):
    text: str


@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserRegistration):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    users_db[user.username] = {
        "username": user.username,
        "password": hashed_password,
        "token": "",
    }
    return {"message": "User registered successfully"}


@app.post("/login", status_code=status.HTTP_200_OK)
async def login(user: UserLogin):
    db_user = users_db.get(user.username)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not bcrypt.checkpw(user.password.encode(), db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Simulate generating a token
    token = f"token_{user.username}"
    users_db[user.username][token] = token
    return {"message": "Login successful"}


@app.post("/translate", status_code=200)
async def translate(request: TranslationRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="No text provided for translation")

    translated_text = f"Translated: {request.text}"

    return {"message": "Translation successful", "translated_text": translated_text}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
