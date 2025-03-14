from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import date


class TourBase(BaseModel):
    name: str
    description: str
    country: str
    city: str
    start_date: date
    end_date: date
    price: float
    type: str  # beach, excursion, ski, etc.
    accommodation_details: Optional[str] = None
    included_services: Optional[str] = None


class TourCreate(TourBase):
    photos: Optional[List[str]] = []
    tour_program: Optional[Dict[str, str]] = {}  # По дням программа тура


class TourUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    price: Optional[float] = None
    photos: Optional[List[str]] = None
    type: Optional[str] = None
    tour_program: Optional[Dict[str, str]] = None
    accommodation_details: Optional[str] = None
    included_services: Optional[str] = None
    is_active: Optional[bool] = None


class TourInDBBase(TourBase):
    id: int
    photos: List[str]
    tour_program: Dict[str, str]
    is_active: bool

    class Config:
        orm_mode = True


class Tour(TourInDBBase):
    pass


class TourWithReviews(Tour):
    average_rating: Optional[float] = None
    review_count: int = 0 