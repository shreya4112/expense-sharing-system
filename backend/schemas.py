from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name: str

class GroupCreate(BaseModel):
    name: str
    users: List[int]

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    paid_by: int
    split_between: List[int]
