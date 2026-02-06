# expenses/routes.py
from fastapi import APIRouter, Depends
from expenses.models import ExpenseCreate
from expenses.services import (
    add_expense,
    get_expenses_by_month,
    get_monthly_expense_total
)
from auth.dependencies import get_current_user

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/")
def create_expense(
    expense: ExpenseCreate,
    username: str = Depends(get_current_user)
):
    return add_expense(username, expense)

@router.get("/monthly")
def monthly_expenses(
    year: int,
    month: int,
    username: str = Depends(get_current_user)
):
    return get_expenses_by_month(username, year, month)

@router.get("/monthly/total")
def monthly_total(
    year: int,
    month: int,
    username: str = Depends(get_current_user)
):
    return {
        "year": year,
        "month": month,
        "total_expenses": get_monthly_expense_total(username, year, month)
    }
