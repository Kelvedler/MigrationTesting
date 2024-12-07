from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Posts(Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    author: Mapped["Users"] = relationship(back_populates="posts")
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
