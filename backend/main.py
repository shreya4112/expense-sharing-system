from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Sharing App")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user.name)

@app.post("/groups")
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    return crud.create_group(db, group.name)

@app.post("/expenses")
def add_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    split_amount = expense.amount / len(expense.split_between)

    for user_id in expense.split_between:
        if user_id != expense.paid_by:
            balance = models.Balance(
                user_owes=user_id,
                user_gets=expense.paid_by,
                amount=split_amount
            )
            db.add(balance)

    db.commit()
    return {"message": "Expense added and balances updated"}
