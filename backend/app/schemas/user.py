from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
import re


class UserBase(BaseModel):
    email: EmailStr
    phone: Optional[str] = None
    first_name: str
    last_name: str

    @validator('phone')
    def phone_validator(cls, v):
        if v is None:
            return v
        # Проверка, что телефон соответствует формату +X-XXX-XXX-XXXX или похожему
        pattern = r'^\+?[0-9]{1,3}[-\s]?[0-9]{3}[-\s]?[0-9]{3}[-\s]?[0-9]{4}$'
        if not re.match(pattern, v):
            raise ValueError('Неверный формат телефона')
        return v


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = Field(None, min_length=8)

    @validator('phone')
    def phone_validator(cls, v):
        if v is None:
            return v
        pattern = r'^\+?[0-9]{1,3}[-\s]?[0-9]{3}[-\s]?[0-9]{3}[-\s]?[0-9]{4}$'
        if not re.match(pattern, v):
            raise ValueError('Неверный формат телефона')
        return v


class UserInDBBase(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str 