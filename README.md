# expense-sharing-system
A backend-first expense sharing application inspired by Splitwise, built using FastAPI and React. Supports group creation, shared expenses, balance tracking, and settlements with clean, scalable architecture.


expense-sharing-app/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── requirements.txt
│
├── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── main.jsx
        ├── App.jsx
        └── api.js


# Expense Sharing Application

A simplified Splitwise-like expense sharing application.

## Features
- Create users and groups
- Add shared expenses
- Equal split logic
- Automatic balance tracking
- Backend-first design

## Tech Stack
- Backend: FastAPI, SQLite
- Frontend: React (Vite)

## Design Decisions
- Used FastAPI for clean REST APIs
- SQLite for simplicity and portability
- ORM-based balance tracking
- Easily extendable for exact and percentage splits
