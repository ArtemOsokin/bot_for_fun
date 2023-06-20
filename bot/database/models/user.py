from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from bot.database.models.main import Base


class User(Base):
    __tablename__ = "user_account"

    tg_id: Mapped[int] = mapped_column(Integer, unique=True)

    first_name: Mapped[str] = mapped_column(String(30), nullable=True)
    last_name: Mapped[str] = mapped_column(String(30), nullable=True)
    username: Mapped[str] = mapped_column(String(30), nullable=True)

    def __repr__(self) -> str:
        return (
            f"User(id={self.id!r}, tg_id={self.tg_id}, "
            f"name={self.first_name!r}, fullname={self.last_name!r})"
        )
