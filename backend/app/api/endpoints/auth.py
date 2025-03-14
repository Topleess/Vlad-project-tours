from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core import security
from app.core.config import settings

router = APIRouter()


@router.post("/login", response_model=schemas.Token)
def login_access_token(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    Получение токена OAuth2 для аутентификации
    """
    user = crud.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Неверный email или пароль")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Неактивный пользователь")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/signup", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Создание нового пользователя
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="Пользователь с таким email уже существует",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.post("/password-recovery/{email}", response_model=schemas.Token)
def recover_password(email: str, db: Session = Depends(deps.get_db)) -> Any:
    """
    Восстановление пароля (упрощенно, в реальности здесь была бы отправка email)
    """
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="Пользователь с таким email не найден",
        )
    password_reset_token = security.create_access_token(
        user.id, expires_delta=timedelta(hours=24)
    )
    # Здесь должна быть логика отправки email с токеном
    # Но для упрощения просто вернем токен, который можно использовать
    # для сброса пароля
    return {"access_token": password_reset_token, "token_type": "bearer"} 