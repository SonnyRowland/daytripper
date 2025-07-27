from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

engine = create_engine(
    "postgresql://daytripper_user:postgres@postgres:5432/daytripper_db"
)

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


def write_to_db(res):
    with Session(engine) as session:
        for pub in res:
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


pub_names = []
pub_addresses = []

try:
    driver = webdriver.Chrome()
    driver.get("https://www.london.camra.org.uk/viewnode.php?id=105284")

    pub_names = driver.find_elements(By.CSS_SELECTOR, "a.title.listitem.pub-guide")
    pub_names_text = [name.text for name in pub_names]

    locations = driver.find_elements(
        By.CSS_SELECTOR, "span[data-lat][data-lng].location"
    )

    for i in range(len(locations)):
        lat = locations[i].get_attribute("data-lat")
        lng = locations[i].get_attribute("data-lng")
        full_address = locations[i].text.strip()
        address = " ".join(full_address.split()[:-2])
        postcode = " ".join(full_address.split()[-2:])

        res.append(
            {
                "name": pub_names_text[i],
                "address": address,
                "postcode": postcode,
                "lat": float(lat),
                "lng": float(lng),
            }
        )

    driver.quit()
    write_to_db(res)
except Exception as e:
    print(e)
