from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class UserBase(DeclarativeBase):
    pass


class User(UserBase):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(125), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(256))
    email: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    is_varified: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self) -> str:
        return f'{self.id} -> {self.username}, {self.email}.'
