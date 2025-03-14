from pydantic import BaseModel
from typing import Dict, Optional, Any
from datetime import datetime


class BookingBase(BaseModel):
    tour_id: int
    travel_date: datetime
    num_people: int
    room_type: str
    additional_services: Optional[Dict[str, Any]] = {}
    total_price: float
    notes: Optional[str] = None


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BaseModel):
    travel_date: Optional[datetime] = None
    num_people: Optional[int] = None
    room_type: Optional[str] = None
    additional_services: Optional[Dict[str, Any]] = None
    total_price: Optional[float] = None
    status: Optional[str] = None
    payment_info: Optional[Dict[str, Any]] = None
    notes: Optional[str] = None


class BookingInDBBase(BookingBase):
    id: int
    user_id: int
    booking_date: datetime
    status: str
    payment_info: Optional[Dict[str, Any]] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class Booking(BookingInDBBase):
    pass


class BookingWithDetails(Booking):
    tour: Dict[str, Any]
    user: Dict[str, Any] 