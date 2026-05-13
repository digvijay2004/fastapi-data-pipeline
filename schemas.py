from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User schemas
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# Item schemas
class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    owner_id: int

class ItemResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None