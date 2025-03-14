from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, Text, ForeignKey, JSON, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from app.db.database import Base


class BookingStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    paid = "paid"
    cancelled = "cancelled"
    completed = "completed"


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    tour_id = Column(Integer, ForeignKey("tours.id"))
    booking_date = Column(DateTime(timezone=True), server_default=func.now())
    travel_date = Column(DateTime(timezone=True))
    num_people = Column(Integer)
    room_type = Column(String)  # standard, deluxe, etc.
    additional_services = Column(JSON, default={})  # Extra services like insurance, excursions
    total_price = Column(Float)
    status = Column(String, default=BookingStatus.pending.value)
    payment_info = Column(JSON, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Отношения
    user = relationship("User", backref="bookings")
    tour = relationship("Tour", backref="bookings") 