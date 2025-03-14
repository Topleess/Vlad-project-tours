import logging
import os
import sys
import time
import uvicorn
from pathlib import Path

# Добавляем текущую директорию в PYTHONPATH
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.db.migrations import run_migrations
from app.db.init_db import init_db
from app.db.database import SessionLocal
from app.core.config import settings


def start():
    """
    Запускает приложение, выполняя следующие шаги:
    1. Запускает миграции базы данных
    2. Инициализирует базу данных тестовыми данными (если нужно)
    3. Запускает API-сервер
    """
    logging.info("Запуск приложения...")
    
    # Создаем директорию versions для миграций, если ее нет
    alembic_versions_dir = Path(__file__).resolve().parent / "alembic" / "versions"
    if not alembic_versions_dir.exists():
        alembic_versions_dir.mkdir(exist_ok=True)
        logging.info(f"Создана директория для миграций: {alembic_versions_dir}")
    
    # Запускаем миграции
    logging.info("Запуск миграций базы данных...")
    try:
        run_migrations()
    except Exception as e:
        logging.error(f"Ошибка при выполнении миграций: {e}")
        sys.exit(1)
    
    # Инициализируем базу данных
    logging.info("Инициализация базы данных...")
    try:
        db = SessionLocal()
        init_db(db)
    except Exception as e:
        logging.error(f"Ошибка при инициализации базы данных: {e}")
        sys.exit(1)
    finally:
        db.close()
    
    # Запускаем API-сервер
    logging.info(f"Запуск API-сервера на http://{settings.HOST}:{settings.PORT}")
    uvicorn.run(
        "app.api.api:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    start() 