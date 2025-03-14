from sqlalchemy import Boolean, Column, Integer, String, Float, Date, DateTime, Text, ForeignKey, JSON, Enum
from sqlalchemy.sql import func
import enum
from app.db.database import Base


class TourType(enum.Enum):
    beach = "beach"
    excursion = "excursion"
    ski = "ski"
    cruise = "cruise"
    adventure = "adventure"
    cultural = "cultural"
    spa = "spa"
    other = "other"


class Tour(Base):
    __tablename__ = "tours"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    country = Column(String, index=True)
    city = Column(String, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    price = Column(Float)
    photos = Column(JSON, default=[])
    type = Column(String, index=True)  # beach, excursion, ski, etc.
    tour_program = Column(JSON, default={})  # По дням программа тура
    accommodation_details = Column(Text)
    included_services = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 