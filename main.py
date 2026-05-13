from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import items, users
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Data Pipeline",
    description="Production-grade REST API with PostgreSQL, authentication, and data pipelines",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/")
def root():
    return {"message": "FastAPI Data Pipeline is running!"}

@app.get("/health")
def health():
    return {"status": "healthy"}