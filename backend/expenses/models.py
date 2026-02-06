# expenses/models.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=2, max_length=30)
    description: Optional[str] = Field(None, max_length=100)
    _date: Optional[date] = None
