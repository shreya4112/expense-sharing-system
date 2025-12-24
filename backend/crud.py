from sqlalchemy.orm import Session
from models import User, Group, Expense, Balance

def create_user(db: Session, name: str):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_group(db: Session, name: str):
    group = Group(name=name)
    db.add(group)
    db.commit()
    db.refresh(group)
    return group

def add_expense(db: Session, data):
    expense = Expense(**data)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense
