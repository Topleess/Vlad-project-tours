from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/tour/{tour_id}", response_model=List[schemas.ReviewWithUserInfo])
def read_tour_reviews(
    *,
    db: Session = Depends(deps.get_db),
    tour_id: int,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Получение всех отзывов для конкретного тура
    """
    # Проверка наличия тура
    tour = crud.tour.get(db, id=tour_id)
    if not tour:
        raise HTTPException(status_code=404, detail="Тур не найден")
        
    reviews = crud.review.get_reviews_with_user_info(db, tour_id=tour_id, skip=skip, limit=limit)
    return reviews


@router.get("/user/me", response_model=List[schemas.Review])
def read_user_reviews(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Получение всех отзывов текущего пользователя
    """
    reviews = crud.review.get_by_user(db, user_id=current_user.id)
    return reviews


@router.post("/", response_model=schemas.Review)
def create_review(
    *,
    db: Session = Depends(deps.get_db),
    review_in: schemas.ReviewCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Создание нового отзыва
    """
    # Проверка наличия тура
    tour = crud.tour.get(db, id=review_in.tour_id)
    if not tour:
        raise HTTPException(status_code=404, detail="Тур не найден")
    
    # Проверка, что у пользователя есть завершенное бронирование этого тура
    bookings = crud.booking.get_by_user(db, user_id=current_user.id)
    has_completed_booking = any(
        b.tour_id == review_in.tour_id and b.status in ["completed", "paid"]
        for b in bookings
    )
    
    if not has_completed_booking and not current_user.is_admin:
        raise HTTPException(
            status_code=400,
            detail="Вы можете оставить отзыв только о турах, которые вы забронировали и оплатили"
        )
    
    # Проверка, что пользователь еще не оставлял отзыв на этот тур
    existing_review = db.query(models.Review).filter(
        models.Review.user_id == current_user.id,
        models.Review.tour_id == review_in.tour_id
    ).first()
    
    if existing_review:
        raise HTTPException(
            status_code=400,
            detail="Вы уже оставили отзыв на этот тур"
        )
    
    review = crud.review.create_with_user(db=db, obj_in=review_in, user_id=current_user.id)
    return review


@router.put("/{review_id}", response_model=schemas.Review)
def update_review(
    *,
    db: Session = Depends(deps.get_db),
    review_id: int,
    review_in: schemas.ReviewUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Обновление отзыва
    """
    review = crud.review.get(db=db, id=review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Отзыв не найден")
    
    # Проверка, что отзыв принадлежит текущему пользователю или пользователь - админ
    if review.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Недостаточно прав для изменения этого отзыва")
    
    review = crud.review.update(db=db, db_obj=review, obj_in=review_in)
    return review


@router.delete("/{review_id}", response_model=schemas.Review)
def delete_review(
    *,
    db: Session = Depends(deps.get_db),
    review_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Удаление отзыва
    """
    review = crud.review.get(db=db, id=review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Отзыв не найден")
    
    # Проверка, что отзыв принадлежит текущему пользователю или пользователь - админ
    if review.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Недостаточно прав для удаления этого отзыва")
    
    review = crud.review.remove(db=db, id=review_id)
    return review 