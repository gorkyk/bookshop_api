from pydantic import BaseModel
from typing import List


class BookRequest(BaseModel):
    id: int
    quantity: int


class AddOrderRequest(BaseModel):
    id: int
    user_id: int
    books: List[BookRequest]
