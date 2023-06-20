from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from bot.database.models.main import Base


class User(Base):
    __tablename__ = "user_account"

    tg_id: Mapped[int] = mapped_column(Integer, unique=True)

    first_name: Mapped[str] = mapped_column(String(30), nullable=True)
    last_name: Mapped[str] = mapped_column(String(30), nullable=True)
    username: Mapped[str] = mapped_column(String(30), nullable=True)
