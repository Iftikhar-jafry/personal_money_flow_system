from incomes.models import IncomeCreate
from datetime import date
import uuid
import json

FileIncome="incomes.json"

def load_income():
    with open(FileIncome,"r") as f:
        return json.load(f)

def save_income(data):
    with open(FileIncome,"w") as f:
        json.dump(FileIncome,data, indent=4)


def add_income(username: str, income: IncomeCreate):
    data = load_income()

    record = {
        "id": str(uuid.uuid4()),
        "username": username,
        "amount": income.amount,
        "source": income.source,
        "date": (income._date or date.today()).isoformat()
    }

    data.append(record)
    save_income(data)
    return record

def get_income_by_month(username: str, year: int, month: int):
    data = load_income()
    result = []

    for item in data:
        if item["username"] != username:
            continue

        y, m, _ = item["date"].split("-")
        if int(y) == year and int(m) == month:
            result.append(item)

    return result

def get_monthly_total(username: str, year: int, month: int):
    incomes = get_income_by_month(username, year, month)
    return sum(i["amount"] for i in incomes)
