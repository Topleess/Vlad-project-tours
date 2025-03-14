from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func

from app.crud.base import CRUDBase
from app.models.review import Review
from app.models.user import User
from app.schemas.review import ReviewCreate, ReviewUpdate


class CRUDReview(CRUDBase[Review, ReviewCreate, ReviewUpdate]):
    def create_with_user(
        self, db: Session, *, obj_in: ReviewCreate, user_id: int
    ) -> Review:
        obj_in_data = obj_in.dict()
        db_obj = Review(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Review]:
        return (
            db.query(Review)
            .filter(Review.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_tour(
        self, db: Session, *, tour_id: int, skip: int = 0, limit: int = 100
    ) -> List[Review]:
        return (
            db.query(Review)
            .filter(Review.tour_id == tour_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_reviews_with_user_info(
        self, db: Session, *, tour_id: int, skip: int = 0, limit: int = 100
    ) -> List[Dict[str, Any]]:
        reviews = (
            db.query(Review)
            .options(joinedload(Review.user))
            .filter(Review.tour_id == tour_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        
        result = []
        for review in reviews:
            result.append({
                "id": review.id,
                "user_id": review.user_id,
                "tour_id": review.tour_id,
                "rating": review.rating,
                "comment": review.comment,
                "created_at": review.created_at,
                "updated_at": review.updated_at,
                "user_name": f"{review.user.first_name} {review.user.last_name}"
            })
            
        return result
    
    def get_average_rating(self, db: Session, *, tour_id: int) -> Optional[float]:
        result = db.query(func.avg(Review.rating)).filter(Review.tour_id == tour_id).scalar()
        return float(result) if result else None


review = CRUDReview(Review) 