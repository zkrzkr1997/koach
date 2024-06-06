from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class UserInDB(User):
    hashed_password: str
    user_id: str


class UserRegister(User):
    username: str
    password: str
