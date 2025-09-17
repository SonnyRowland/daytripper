import json

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

from app.config import settings

engine = create_engine(settings.database_url)

res = []


class Base(DeclarativeBase):
    pass


class Pub(Base):
    __tablename__ = "camra_pubs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str]
    postcode: Mapped[str]
    lat: Mapped[float]
    lng: Mapped[float]


pubs_table = Pub.__table__

Base.metadata.create_all(engine)


def write_to_db():
    data = []

    with open("app/data/sample_data.json") as f:
        data = f.read()

    parsed_data = json.loads(data)

    with Session(engine) as session:
        session.query(Pub).delete()
        session.commit()
        for pub in parsed_data:
            try:
                session.add(
                    Pub(
                        name=pub["name"],
                        address=pub["address"],
                        postcode=pub["postcode"],
                        lat=pub["lat"],
                        lng=pub["lng"],
                    )
                )
                session.commit()
            except Exception as e:
                print(e)


write_to_db()
