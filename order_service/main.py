from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()


class Order(BaseModel):
    id: int
    user_id: int
    item: str


orders_db = []

USER_SERVICE_URL = "http://user_service:8001"


@app.post("/orders/")
async def create_order(order: Order):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{USER_SERVICE_URL}/users/{order.user_id}")
        if res.status_code != 200:
            return {"error": "User not found"}
        user_data = res.json()

    orders_db.append(order)
    return {
        "order": order,
        "user": user_data
    }
