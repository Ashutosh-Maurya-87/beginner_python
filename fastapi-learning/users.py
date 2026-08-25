from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from pydantic import Field

app = APIRouter()


class User(BaseModel):
    name: str
    # age: int = Field(gt=0, lt=120)   # gt -> greater than, lt -> less than
    age: int = Field(
        ge=18, le=60
    )  # ge -> greater than equal to, le -> less than equal to
    address: str


@app.get("/all_users")
def users():
    return {"users": [{"id": 1, "name": "Ashutosh"}, {"id": 2, "name": "Alisha"}]}


@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "name": user.name,
        "age": user.age,
        "address": user.address,
    }

