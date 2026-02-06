# income/routes.py
from fastapi import APIRouter, Depends
from incomes.models import IncomeCreate
from incomes.services import add_income, get_income_by_month, get_monthly_total
from auth.dependencies import get_current_user

router = APIRouter(prefix="/income", tags=["Income"])

@router.post("/")
def create_income(income:IncomeCreate,username: str = Depends(get_current_user)):
    print("hello")
    return add_income(username,income.amount,income.source,income._date)

@router.get("/monthly")
def monthly_income(
    year: int,
    month: int,
    username: str = Depends(get_current_user)
):
    return get_income_by_month(username, year, month)

@router.get("/monthly/total")
def monthly_total(
    year: int,
    month: int,
    username: str = Depends(get_current_user)
):
    return {
        "year": year,
        "month": month,
        "total_income": get_monthly_total(username, year, month)
    }
