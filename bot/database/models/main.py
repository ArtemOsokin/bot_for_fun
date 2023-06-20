from datetime import datetime as dt

from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    created_at: Mapped[dt] = mapped_column(insert_default=dt.now())
    updated_at: Mapped[dt] = mapped_column(insert_default=dt.now(), onupdate=dt.now())
