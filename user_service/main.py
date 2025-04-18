from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users_db.get(user_id)
    if user:
        return user
    return {"error": "User not found"}
