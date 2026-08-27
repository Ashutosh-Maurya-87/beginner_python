from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from pydantic import Field

app = APIRouter(prefix="/users", tags=["Users"])


class User(BaseModel):
    id: int
    name: str
    # age: int = Field(gt=0, lt=120)   # gt -> greater than, lt -> less than
    age: int = Field(
        ge=18, le=60
    )  # ge -> greater than equal to, le -> less than equal to
    address: str


userData = [
    {"id": 1, "name": "Ashutosh", "age": 26, "address": "Coder wali gali"},
    {"id": 2, "name": "Alisha", "age": 25, "address": "Baju wali gali"},
]


@app.get("/all_users")
def users():
    return {"data": userData, "message": "Getting all user successfully"}


@app.post("/create_user")
def create_user(user: User):
    newUser = {
        "id": user.id,
        "name": user.name,
        "age": user.age,
        "address": user.address,
    }
    userData.append(newUser)
    return {"message": "User created Successfully", "new_user": newUser}
