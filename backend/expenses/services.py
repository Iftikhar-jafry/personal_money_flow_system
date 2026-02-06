# expenses/service.py
import json
import uuid
from datetime import date
from expenses.models import ExpenseCreate

EXPENSE_FILE = "expenses.json"

def load_expenses():
    with open(EXPENSE_FILE, "r") as f:
        return json.load(f)

def save_expenses(data):
    with open(EXPENSE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(username: str, expense: ExpenseCreate):
    data = load_expenses()

    record = {
        "id": str(uuid.uuid4()),
        "username": username,
        "amount": expense.amount,
        "category": expense.category,
        "description": expense.description,
        "date": (expense.date or date.today()).isoformat()
    }

    data.append(record)
    save_expenses(data)
    return record

def get_expenses_by_month(username: str, year: int, month: int):
    data = load_expenses()
    result = []

    for e in data:
        if e["username"] != username:
            continue

        y, m, _ = e["date"].split("-")
        if int(y) == year and int(m) == month:
            result.append(e)

    return result

def get_monthly_expense_total(username: str, year: int, month: int):
    expenses = get_expenses_by_month(username, year, month)
    return sum(e["amount"] for e in expenses)
