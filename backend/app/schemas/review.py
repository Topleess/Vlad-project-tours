from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ReviewBase(BaseModel):
    tour_id: int
    rating: int = Field(..., ge=1, le=5)  # rating from 1 to 5
    comment: str


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    rating: Optional[int] = Field(None, ge=1, le=5)
    comment: Optional[str] = None


class ReviewInDBBase(ReviewBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class Review(ReviewInDBBase):
    pass


class ReviewWithUserInfo(Review):
    user_name: str  # First name + last name of the reviewer 