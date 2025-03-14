from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Booking])
def read_bookings(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Получение списка всех бронирований (только для администраторов)
    """
    bookings = crud.booking.get_multi(db, skip=skip, limit=limit)
    return bookings


@router.get("/my", response_model=List[schemas.Booking])
def read_user_bookings(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Получение списка бронирований текущего пользователя
    """
    bookings = crud.booking.get_by_user(db, user_id=current_user.id)
    return bookings


@router.get("/{booking_id}", response_model=schemas.BookingWithDetails)
def read_booking(
    *,
    db: Session = Depends(deps.get_db),
    booking_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Получение информации о конкретном бронировании
    """
    booking_data = crud.booking.get_booking_with_details(db, booking_id=booking_id)
    if not booking_data:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    
    # Проверка, что бронирование принадлежит текущему пользователю или пользователь - админ
    if booking_data["user_id"] != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Недостаточно прав для просмотра этого бронирования")
    
    return booking_data


@router.post("/", response_model=schemas.Booking)
def create_booking(
    *,
    db: Session = Depends(deps.get_db),
    booking_in: schemas.BookingCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Создание нового бронирования
    """
    # Проверка наличия тура
    tour = crud.tour.get(db, id=booking_in.tour_id)
    if not tour:
        raise HTTPException(status_code=404, detail="Тур не найден")
    
    # Проверка активности тура
    if not tour.is_active:
        raise HTTPException(status_code=400, detail="Этот тур недоступен для бронирования")
    
    booking = crud.booking.create_with_user(db=db, obj_in=booking_in, user_id=current_user.id)
    return booking


@router.put("/{booking_id}/status", response_model=schemas.Booking)
def update_booking_status(
    *,
    db: Session = Depends(deps.get_db),
    booking_id: int,
    status: str,
    current_user: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Обновление статуса бронирования (только для администраторов)
    """
    booking = crud.booking.update_status(db=db, booking_id=booking_id, new_status=status)
    if not booking:
        raise HTTPException(status_code=404, detail="Бронирование не найдено или неверный статус")
    return booking


@router.delete("/{booking_id}", response_model=schemas.Booking)
def cancel_booking(
    *,
    db: Session = Depends(deps.get_db),
    booking_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Отмена бронирования
    """
    booking = crud.booking.get(db=db, id=booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    
    # Проверка, что бронирование принадлежит текущему пользователю или пользователь - админ
    if booking.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Недостаточно прав для отмены этого бронирования")
    
    # Проверка статуса (нельзя отменить уже оплаченное бронирование для обычных пользователей)
    if booking.status == "paid" and not current_user.is_admin:
        raise HTTPException(status_code=400, detail="Нельзя отменить оплаченное бронирование")
    
    booking = crud.booking.update_status(db=db, booking_id=booking_id, new_status="cancelled")
    return booking 