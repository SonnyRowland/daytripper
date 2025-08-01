"""Database model for geographical places and locations"""

from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Place(Base):
    """Represents a geographical location or point of interest.

    Contains location data including coordinates for mapping
    and postcode for external API lookup.
    """

    __tablename__ = "camra_pubs"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str]
    postcode: Mapped[str]
    lat: Mapped[float]
    lng: Mapped[float]
