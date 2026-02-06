# income/models.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class IncomeCreate(BaseModel):
    amount: float = Field(..., gt=0)
    source: str = Field(..., min_length=2, max_length=50)
    _date: Optional[date] = None
