# FastAPI Data Pipeline

Production-grade REST API built with FastAPI, SQLAlchemy, and SQLite.

## Tech Stack
- **FastAPI** — REST API framework
- **SQLAlchemy** — ORM for database management
- **SQLite** — Lightweight database
- **Pydantic** — Data validation
- **Uvicorn** — ASGI server

## Features
- Full CRUD operations for Users and Items
- Password hashing for security
- Pydantic data validation
- Interactive Swagger UI docs
- Modular router architecture

## Setup
1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install: `pip install -r requirements.txt`
5. Run: `uvicorn main:app --reload`
6. Visit: `http://127.0.0.1:8000/docs`

## API Endpoints
### Users
- `POST /users/` — Create user
- `GET /users/` — Get all users
- `GET /users/{id}` — Get user by ID
- `DELETE /users/{id}` — Delete user

### Items
- `POST /items/` — Create item
- `GET /items/` — Get all items
- `GET /items/{id}` — Get item by ID
- `PUT /items/{id}` — Update item
- `DELETE /items/{id}` — Delete item