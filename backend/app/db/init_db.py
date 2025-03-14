import logging
from sqlalchemy.orm import Session
from datetime import date, datetime, timedelta
import json

from app import crud, schemas
from app.core.config import settings
from app.db.database import Base, engine
from app.models import User, Tour, Booking, Review


# создаем все таблицы
def init_db(db: Session) -> None:
    # Создаем таблицы
    Base.metadata.create_all(bind=engine)
    
    # Проверяем, есть ли в базе хотя бы один админ
    user = crud.user.get_by_email(db, email="admin@example.com")
    if not user:
        user_in = schemas.UserCreate(
            first_name="Admin",
            last_name="User",
            email="admin@example.com",
            password="admin123",
            phone="+7-999-123-4567"
        )
        user = crud.user.create(db, obj_in=user_in)
        
        # Делаем пользователя админом
        user.is_admin = True
        db.add(user)
        db.commit()
        db.refresh(user)
        
        logging.info("Создан администратор: admin@example.com / admin123")
    
    # Добавляем тестового пользователя если его нет
    user = crud.user.get_by_email(db, email="user@example.com")
    if not user:
        user_in = schemas.UserCreate(
            first_name="Test",
            last_name="User",
            email="user@example.com",
            password="user123",
            phone="+7-999-765-4321"
        )
        user = crud.user.create(db, obj_in=user_in)
        logging.info("Создан тестовый пользователь: user@example.com / user123")
    
    # Добавляем тестовые туры если их нет
    if db.query(Tour).count() == 0:
        # Тур 1: Пляжный отдых в Турции
        tour1 = Tour(
            name="Пляжный отдых в Анталии",
            description="Насладитесь прекрасными пляжами и теплым морем на курортах Турции. В стоимость включены: перелет, трансфер, проживание в отеле 5* по системе «Все включено».",
            country="Турция",
            city="Анталия",
            start_date=date.today() + timedelta(days=30),
            end_date=date.today() + timedelta(days=37),
            price=75000.0,
            photos=json.dumps(["turkey1.jpg", "turkey2.jpg", "turkey3.jpg"]),
            type="beach",
            tour_program=json.dumps({
                "1": "Прибытие, заселение в отель, приветственный ужин",
                "2": "Отдых на пляже, вечерняя анимация",
                "3": "Экскурсия в старый город",
                "4-6": "Свободное время, отдых на пляже",
                "7": "Прощальный ужин",
                "8": "Выезд из отеля, трансфер в аэропорт"
            }),
            accommodation_details="Отель 5*, номер Deluxe с видом на море, все включено",
            included_services="Перелет, трансфер, проживание, питание по системе «Все включено», страховка",
            is_active=True
        )
        
        # Тур 2: Экскурсионный тур по Италии
        tour2 = Tour(
            name="Классическая Италия",
            description="Увлекательное путешествие по историческим городам Италии. Вы посетите Рим, Флоренцию и Венецию, увидите главные достопримечательности и погрузитесь в атмосферу итальянской культуры.",
            country="Италия",
            city="Рим, Флоренция, Венеция",
            start_date=date.today() + timedelta(days=45),
            end_date=date.today() + timedelta(days=52),
            price=95000.0,
            photos=json.dumps(["italy1.jpg", "italy2.jpg", "italy3.jpg"]),
            type="excursion",
            tour_program=json.dumps({
                "1": "Прибытие в Рим, заселение в отель",
                "2": "Обзорная экскурсия по Риму, посещение Колизея и Римского форума",
                "3": "Ватикан, музеи Ватикана, собор Святого Петра",
                "4": "Переезд во Флоренцию, обзорная экскурсия",
                "5": "Свободный день во Флоренции",
                "6": "Переезд в Венецию, обзорная экскурсия",
                "7": "Свободный день в Венеции",
                "8": "Выезд из отеля, трансфер в аэропорт"
            }),
            accommodation_details="Отели 4*, стандартные номера",
            included_services="Перелет, трансфер, проживание с завтраками, экскурсии по программе, услуги гида, страховка",
            is_active=True
        )
        
        # Тур 3: Горнолыжный курорт
        tour3 = Tour(
            name="Горнолыжный отдых в Альпах",
            description="Потрясающий отдых на лучших трассах французских Альп. Идеально подходит как для начинающих, так и для опытных лыжников.",
            country="Франция",
            city="Шамони",
            start_date=date.today() + timedelta(days=90),  # Зимний тур
            end_date=date.today() + timedelta(days=97),
            price=120000.0,
            photos=json.dumps(["ski1.jpg", "ski2.jpg", "ski3.jpg"]),
            type="ski",
            tour_program=json.dumps({
                "1": "Прибытие, заселение в отель, подбор снаряжения",
                "2": "Инструктаж, катание на начальных трассах",
                "3-6": "Катание на трассах различной сложности",
                "7": "Свободное время, прощальный ужин",
                "8": "Выезд из отеля, трансфер в аэропорт"
            }),
            accommodation_details="Горный шале 4*, двухместные номера",
            included_services="Перелет, трансфер, проживание, завтраки и ужины, ски-пасс на 6 дней, страховка",
            is_active=True
        )
        
        db.add(tour1)
        db.add(tour2)
        db.add(tour3)
        db.commit()
        logging.info("Добавлены тестовые туры")
        
        # Добавляем тестовые бронирования
        test_user = crud.user.get_by_email(db, email="user@example.com")
        admin_user = crud.user.get_by_email(db, email="admin@example.com")
        
        booking1 = Booking(
            user_id=test_user.id,
            tour_id=1,  # Тур в Турцию
            booking_date=datetime.now() - timedelta(days=10),
            travel_date=datetime.now() + timedelta(days=30),
            num_people=2,
            room_type="Deluxe",
            additional_services=json.dumps({
                "transfer_type": "Индивидуальный",
                "insurance": True,
                "excursions": ["Памуккале", "Демре-Мира-Кекова"]
            }),
            total_price=160000.0,  # За двоих
            status="confirmed",
            payment_info=json.dumps({
                "payment_method": "Кредитная карта",
                "payment_id": "TEST12345",
                "payment_date": (datetime.now() - timedelta(days=9)).isoformat()
            }),
            notes="Предпочтение - номер на высоком этаже"
        )
        
        booking2 = Booking(
            user_id=admin_user.id,
            tour_id=2,  # Тур по Италии
            booking_date=datetime.now() - timedelta(days=5),
            travel_date=datetime.now() + timedelta(days=45),
            num_people=1,
            room_type="Standard",
            additional_services=json.dumps({
                "transfer_type": "Групповой",
                "insurance": True,
                "excursions": ["Музеи Ватикана", "Галерея Уффици"]
            }),
            total_price=95000.0,
            status="paid",
            payment_info=json.dumps({
                "payment_method": "Банковский перевод",
                "payment_id": "TEST67890",
                "payment_date": (datetime.now() - timedelta(days=3)).isoformat()
            }),
            notes=""
        )
        
        db.add(booking1)
        db.add(booking2)
        db.commit()
        logging.info("Добавлены тестовые бронирования")
        
        # Добавляем тестовые отзывы
        review1 = Review(
            user_id=admin_user.id,
            tour_id=1,  # Отзыв о туре в Турцию
            rating=5,
            comment="Отличный отель, прекрасный сервис, чистый пляж. Очень понравилось!"
        )
        
        db.add(review1)
        db.commit()
        logging.info("Добавлены тестовые отзывы")
    
    logging.info("База данных инициализирована успешно")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    from app.db.database import SessionLocal
    db = SessionLocal()
    init_db(db) 