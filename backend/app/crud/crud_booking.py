from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session, joinedload

from app.crud.base import CRUDBase
from app.models.booking import Booking, BookingStatus
from app.schemas.booking import BookingCreate, BookingUpdate


class CRUDBooking(CRUDBase[Booking, BookingCreate, BookingUpdate]):
    def create_with_user(
        self, db: Session, *, obj_in: BookingCreate, user_id: int
    ) -> Booking:
        obj_in_data = obj_in.dict()
        db_obj = Booking(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Booking]:
        return (
            db.query(Booking)
            .filter(Booking.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_tour(
        self, db: Session, *, tour_id: int, skip: int = 0, limit: int = 100
    ) -> List[Booking]:
        return (
            db.query(Booking)
            .filter(Booking.tour_id == tour_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_status(
        self, db: Session, *, status: str, skip: int = 0, limit: int = 100
    ) -> List[Booking]:
        return (
            db.query(Booking)
            .filter(Booking.status == status)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update_status(
        self, db: Session, *, booking_id: int, new_status: str
    ) -> Optional[Booking]:
        booking = self.get(db, id=booking_id)
        if not booking:
            return None
        
        # Проверка валидности статуса
        if new_status not in [status.value for status in BookingStatus]:
            return None
            
        booking.status = new_status
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking
        
    def get_booking_with_details(self, db: Session, *, booking_id: int) -> Optional[Dict[str, Any]]:
        booking = db.query(Booking).options(
            joinedload(Booking.user),
            joinedload(Booking.tour)
        ).filter(Booking.id == booking_id).first()
        
        if not booking:
            return None
            
        # Формируем данные для ответа
        booking_data = {
            "id": booking.id,
            "user_id": booking.user_id,
            "tour_id": booking.tour_id,
            "booking_date": booking.booking_date,
            "travel_date": booking.travel_date,
            "num_people": booking.num_people,
            "room_type": booking.room_type,
            "additional_services": booking.additional_services,
            "total_price": booking.total_price,
            "status": booking.status,
            "payment_info": booking.payment_info,
            "notes": booking.notes,
            "created_at": booking.created_at,
            "updated_at": booking.updated_at,
            "user": {
                "id": booking.user.id,
                "email": booking.user.email,
                "first_name": booking.user.first_name,
                "last_name": booking.user.last_name,
                "phone": booking.user.phone
            },
            "tour": {
                "id": booking.tour.id,
                "name": booking.tour.name,
                "country": booking.tour.country,
                "city": booking.tour.city,
                "start_date": booking.tour.start_date,
                "end_date": booking.tour.end_date,
                "price": booking.tour.price,
                "type": booking.tour.type
            }
        }
        
        return booking_data


booking = CRUDBooking(Booking) 