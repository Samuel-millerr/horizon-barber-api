from sqlalchemy.orm import Session

from horizon_barber_api.database import engine, get_session
from horizon_barber_api.models import Service
from horizon_barber_api.settings import settings


def create_tables() -> None:
    try:
        settings.DBBaseModel.metadata.create_all(engine)
        print("Tables created")
        insert_data()
        print("Data inserted")
    except Exception as err:
        raise err


def insert_data() -> None:
    try:
        with next(get_session()) as session:
            services = [
                Service(
                    name="Corte Clássico",
                    description="Tesoura ou máquina, acabamento perfeito",
                    price=35.0,
                    duration_minutes=30,
                    icon="✂️",
                ),
                Service(
                    name="Barba Completa",
                    description="Navalha quente + modelagem profissional",
                    price=30.0,
                    duration_minutes=25,
                    icon="🪒",
                ),
                Service(
                    name="Combo Premium",
                    description="Corte + Barba + Lavagem com produtos",
                    price=59.90,
                    duration_minutes=55,
                    icon="💈",
                ),
            ]

            session.add_all(services)
            session.commit()

    except Exception as err:
        raise err


create_tables()
