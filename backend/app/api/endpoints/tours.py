from typing import Any, List, Optional
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Tour])
def read_tours(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    country: Optional[str] = None,
    city: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    tour_type: Optional[str] = None,
) -> Any:
    """
    Получение списка туров с возможностью фильтрации
    """
    tours = crud.tour.search_tours(
        db, 
        country=country,
        city=city,
        min_price=min_price,
        max_price=max_price,
        start_date=start_date,
        end_date=end_date,
        tour_type=tour_type,
        skip=skip, 
        limit=limit
    )
    return tours


@router.get("/{tour_id}", response_model=schemas.TourWithReviews)
def read_tour(
    *,
    db: Session = Depends(deps.get_db),
    tour_id: int,
) -> Any:
    """
    Получение информации о туре по id
    """
    tour_data = crud.tour.get_tour_with_reviews(db, tour_id=tour_id)
    if not tour_data:
        raise HTTPException(status_code=404, detail="Тур не найден")
    return tour_data


@router.post("/", response_model=schemas.Tour)
def create_tour(
    *,
    db: Session = Depends(deps.get_db),
    tour_in: schemas.TourCreate,
    current_user: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Создание нового тура (только для администраторов)
    """
    tour = crud.tour.create(db=db, obj_in=tour_in)
    return tour


@router.put("/{tour_id}", response_model=schemas.Tour)
def update_tour(
    *,
    db: Session = Depends(deps.get_db),
    tour_id: int,
    tour_in: schemas.TourUpdate,
    current_user: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Обновление информации о туре (только для администраторов)
    """
    tour = crud.tour.get(db=db, id=tour_id)
    if not tour:
        raise HTTPException(status_code=404, detail="Тур не найден")
    tour = crud.tour.update(db=db, db_obj=tour, obj_in=tour_in)
    return tour


@router.delete("/{tour_id}", response_model=schemas.Tour)
def delete_tour(
    *,
    db: Session = Depends(deps.get_db),
    tour_id: int,
    current_user: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Удаление тура (только для администраторов)
    """
    tour = crud.tour.get(db=db, id=tour_id)
    if not tour:
        raise HTTPException(status_code=404, detail="Тур не найден")
    tour = crud.tour.remove(db=db, id=tour_id)
    return tour 