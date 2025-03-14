from typing import List, Optional, Dict, Any
from sqlalchemy import func, and_
from sqlalchemy.orm import Session
from datetime import date

from app.crud.base import CRUDBase
from app.models.tour import Tour
from app.models.review import Review
from app.schemas.tour import TourCreate, TourUpdate


class CRUDTour(CRUDBase[Tour, TourCreate, TourUpdate]):
    def get_by_country(self, db: Session, *, country: str, skip: int = 0, limit: int = 100) -> List[Tour]:
        return db.query(Tour).filter(Tour.country == country).offset(skip).limit(limit).all()
    
    def get_by_type(self, db: Session, *, tour_type: str, skip: int = 0, limit: int = 100) -> List[Tour]:
        return db.query(Tour).filter(Tour.type == tour_type).offset(skip).limit(limit).all()
    
    def get_by_price_range(self, db: Session, *, min_price: float, max_price: float, skip: int = 0, limit: int = 100) -> List[Tour]:
        return db.query(Tour).filter(
            Tour.price >= min_price,
            Tour.price <= max_price
        ).offset(skip).limit(limit).all()
    
    def get_by_date_range(self, db: Session, *, start_date: date, end_date: date, skip: int = 0, limit: int = 100) -> List[Tour]:
        return db.query(Tour).filter(
            Tour.start_date >= start_date,
            Tour.end_date <= end_date
        ).offset(skip).limit(limit).all()
    
    def search_tours(self, db: Session, *, country: Optional[str] = None, city: Optional[str] = None, 
                    min_price: Optional[float] = None, max_price: Optional[float] = None,
                    start_date: Optional[date] = None, end_date: Optional[date] = None,
                    tour_type: Optional[str] = None, skip: int = 0, limit: int = 100) -> List[Tour]:
        query = db.query(Tour)
        
        if country:
            query = query.filter(Tour.country == country)
        if city:
            query = query.filter(Tour.city == city)
        if min_price is not None:
            query = query.filter(Tour.price >= min_price)
        if max_price is not None:
            query = query.filter(Tour.price <= max_price)
        if start_date:
            query = query.filter(Tour.start_date >= start_date)
        if end_date:
            query = query.filter(Tour.end_date <= end_date)
        if tour_type:
            query = query.filter(Tour.type == tour_type)
            
        return query.filter(Tour.is_active == True).offset(skip).limit(limit).all()
    
    def get_tour_with_reviews(self, db: Session, *, tour_id: int) -> Dict[str, Any]:
        tour = self.get(db, id=tour_id)
        if not tour:
            return None
        
        # Получаем средний рейтинг и количество отзывов
        result = db.query(
            func.avg(Review.rating).label("average_rating"),
            func.count(Review.id).label("review_count")
        ).filter(Review.tour_id == tour_id).first()
        
        tour_data = {
            "id": tour.id,
            "name": tour.name,
            "description": tour.description,
            "country": tour.country,
            "city": tour.city,
            "start_date": tour.start_date,
            "end_date": tour.end_date,
            "price": tour.price,
            "photos": tour.photos,
            "type": tour.type,
            "tour_program": tour.tour_program,
            "accommodation_details": tour.accommodation_details,
            "included_services": tour.included_services,
            "is_active": tour.is_active,
            "average_rating": float(result.average_rating) if result.average_rating else None,
            "review_count": result.review_count
        }
        
        return tour_data


tour = CRUDTour(Tour) 