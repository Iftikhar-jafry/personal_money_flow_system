# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from auth.routes import router as auth_router
from incomes.routes import router as income_router
from expenses.routes import router as expenses_router  

app = FastAPI(
    title="Personal Finance API",
    description="Track income, expenses and monthly summary",
    version="1.0.0"
)

# -----------------------------
# CORS (important for frontend)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routers
# -----------------------------
app.include_router(auth_router)
app.include_router(income_router)
app.include_router(expenses_router)

# -----------------------------
# Root / Health Check
# -----------------------------
@app.get("/")
def root():
    return {
        "status": "API running",
        "message": "Welcome to Personal Finance API"
    }
