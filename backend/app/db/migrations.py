import subprocess
import logging
import os
import sys
from pathlib import Path


def run_migrations():
    """Запускает миграции базы данных"""
    logging.info("Запуск миграций...")
    
    # Получаем корневую директорию проекта
    backend_dir = Path(__file__).resolve().parent.parent.parent
    
    try:
        # Создаем начальную миграцию, если ее нет
        versions_dir = os.path.join(backend_dir, "alembic", "versions")
        if not os.listdir(versions_dir):
            subprocess.run(
                ["alembic", "revision", "--autogenerate", "-m", "Initial migration"],
                cwd=backend_dir,
                check=True,
            )
            logging.info("Создана начальная миграция")
        
        # Применяем миграции
        subprocess.run(
            ["alembic", "upgrade", "head"],
            cwd=backend_dir,
            check=True,
        )
        logging.info("Миграции успешно применены")
    except subprocess.CalledProcessError as e:
        logging.error(f"Ошибка при выполнении миграций: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Непредвиденная ошибка при выполнении миграций: {e}")
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run_migrations() 